from django.shortcuts import render, redirect

from pos.forms import CategoryForm
from pos.models import Category


# Create your views here.
def category_list(request):
    data = Category.objects.all()
    context = {
        'title':'Add Category',
        'category_list': data,
    }
    return render(request, 'category_list.html', context)

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

    return render(request, 'category_add.html', context)

def category_edit(request, category_id):
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=Category.objects.get(pk=category_id))
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm(instance=Category.objects.get(pk=category_id))
        context = {
            'title': 'Edit Category',
            'form': form,
        }
    return render(request, 'category_edit.html',context)

def category_delete(request, category_id):
    if request.method == 'POST':
        Category.objects.get(pk=category_id).delete()
        return redirect("category_list")
    else:
        form = CategoryForm(instance=Category.objects.get(pk=category_id))
        context = {
            'title': 'Delete Category',
            'form': form,
        }
    return render(request,'category_delete.html',context)