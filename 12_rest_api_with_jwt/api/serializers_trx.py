from rest_framework import serializers
from .models import Transaction, TransactionItem, Customer, Product

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'member']

class TransactionItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )
    product = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TransactionItem
        fields = ['product_id', 'product', 'quantity']

class TransactionSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    products = TransactionItemSerializer(many=True)

    class Meta:
        model = Transaction
        fields = ['id', 'customer', 'products', 'total_amount', 'transaction_date']
        read_only_fields = ['id', 'total_amount', 'transaction_date']