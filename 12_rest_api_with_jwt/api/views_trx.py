from django.db import transaction as django_transaction
from rest_framework import viewsets, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Transaction, TransactionItem, Product
from .serializers_trx import TransactionSerializer, CustomerSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=False, methods=['POST'])
    def create_transaction(self, request):
        try:
            with django_transaction.atomic():  # Gunakan atomic transaction
                # 1. Ambil data dari request
                customer_data = request.data.get('customer')
                product_data = request.data.get('products')

                # 2. Validasi data
                if not customer_data:
                    raise serializers.ValidationError({'customer': 'Data pelanggan tidak boleh kosong.'})

                if not product_data:
                    raise serializers.ValidationError({'products': 'Daftar produk tidak boleh kosong.'})

                # 3. Buat customer baru
                customer_serializer = CustomerSerializer(data=customer_data)
                customer_serializer.is_valid(raise_exception=True)
                customer = customer_serializer.save()

                # 4. Buat transaksi baru
                transaction = Transaction.objects.create(customer=customer)

                total_amount = 0

                # 5. Loop melalui produk-produk yang dibeli
                for item in product_data:
                    product_id = item.get('product_id')
                    quantity = item.get('quantity')

                    # Validasi product_id dan quantity
                    if not product_id or not quantity:
                        raise serializers.ValidationError({'products': 'product_id dan quantity harus diisi.'})
                    if quantity <= 0:
                        raise serializers.ValidationError({'products': 'Jumlah product yang dibeli tidak boleh kurang dari atau sama dengan 0.'})

                    try:
                        product = Product.objects.get(pk=product_id)
                    except Product.DoesNotExist:
                        raise serializers.ValidationError({'products': f'Produk dengan ID {product_id} tidak ditemukan.'})

                    # Validasi dan kurangi stok produk
                    if product.stock < quantity:
                        raise serializers.ValidationError({'products': f'Stok produk {product.name} tidak mencukupi.'})
                    if product.stock - quantity < 0:
                        raise serializers.ValidationError({'products': f'Stok produk {product.name} tidak mencukupi.'})

                    product.stock -= quantity
                    product.save()

                    # Buat TransactionItem
                    transaction_item = TransactionItem.objects.create(
                        transaction=transaction,
                        product=product,
                        quantity=quantity
                    )

                    total_amount += product.price * quantity

                # 6. Update total_amount transaksi
                transaction.total_amount = total_amount
                transaction.save()

            # (Response di luar blok atomic)
            serializer = self.get_serializer(transaction)
            return Response({
                'statusCode': status.HTTP_201_CREATED,
                'message': 'Transaksi berhasil dibuat.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        except serializers.ValidationError as e:
            return Response({
                'statusCode': status.HTTP_400_BAD_REQUEST,
                'message': 'Validasi gagal.',
                'data': e.detail
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                'statusCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'Terjadi kesalahan: {str(e)}',
                'data': []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#  Sample request
# {
#     "customer": {
#         "name": "Pelanggan Baru",
#         "email": "pelanggan@example.com",
#         "phone": "1234567890",
#         "member": false
#     },
#     "products": [
#         {
#             "product_id": 1,
#             "quantity": 2
#         },
#         {
#             "product_id": 2,
#             "quantity": 3
#         }
#     ]
# }