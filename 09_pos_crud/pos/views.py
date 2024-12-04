from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

from pos.forms import CategoryForm, ProductForm, CustomerForm
from pos.models import Category, Product, Customer


# Create your views here.
def category_list(request):
    data = Category.objects.all()
    context = {
        'title':'Add Category',
        'category_list': data,
    }
    return render(request, 'category/category_list.html', context)

def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm()

    context = {
        'title': 'Add Category',
        'form': form,
    }

    return render(request, 'category/category_add.html', context)

def category_edit(request, pk):
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=Category.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm(instance=Category.objects.get(pk=pk))
        context = {
            'title': 'Edit Category',
            'form': form,
        }
    return render(request, 'category/category_edit.html',context)

def category_delete(request, pk):
    if request.method == 'POST':
        Category.objects.get(pk=pk).delete()
        return redirect("category_list")
    else:
        data = Category.objects.get(pk=pk)
        context = {
            'title': 'Delete Category',
            'category': data,
        }
    return render(request,'category/category_delete.html',context)



def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 10)  # 10 produk per halaman

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'product/product_list.html', {'products': products, 'query': query})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product/product_edit.html', {'form': form})

def update_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/product_edit.html', {'form': form})

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product/product_delete.html', {'product': product})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer/customer_add.html', {'form': form})

def update_customer(request, id):
    customer = get_object_or_404(Customer, pk=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/customer_edit.html', {'form': form})

def delete_customer(request, id):
    customer = get_object_or_404(Customer, pk=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customer/customer_delete.html', {'customer': customer})