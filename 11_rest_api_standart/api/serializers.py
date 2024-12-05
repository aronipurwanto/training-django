from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Atau, spesifikkan field yang ingin disertakan: ['id', 'code', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = serializers.StringRelatedField(read_only=True)  # Menampilkan nama kategori saat membaca data

    class Meta:
        model = Product
        fields = ['id', 'name','category', 'category_id', 'price', 'stock', 'description']

    def validate(self, data):
        """
        Validasi data secara keseluruhan.
        """
        if data['price'] <= 0:
            raise serializers.ValidationError("Harga harus lebih besar dari 0.")
        if data['stock'] < 0:
            raise serializers.ValidationError("Stok tidak boleh negatif.")
        # Tambahkan validasi lain sesuai kebutuhan
        return data

    def validate_category_id(self, value):
        """
        Validasi category_id.
        """
        if not Category.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Kategori tidak ditemukan.")
        return value
