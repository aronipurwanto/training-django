from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Atau, spesifikkan field yang ingin disertakan: ['id', 'code', 'name']

class ProductSerializer(serializers.ModelSerializer):
    # category_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all(),
    #     source='category',
    #     write_only=True
    # )
    # ... kode lainnya ...
    category = serializers.StringRelatedField(read_only=True)  # Menampilkan nama kategori saat membaca data
    category_id = serializers.IntegerField(write_only=True)
    #created_by = serializers.SerializerMethodField()
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'category_id', 'price', 'stock', 'description', 'created_by', 'created_at']

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

    def get_created_by(self, obj):
        return obj.created_by.username  # Asumsi model Product memiliki field created_by (ForeignKey ke User)

    def create(self, validated_data):
        product = Product.objects.create(**validated_data, created_by=self.context['request'].user)
        return product
