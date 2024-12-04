from lib2to3.fixes.fix_input import context

from django.shortcuts import render

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
    context = {
        'title': 'Add Category',
    }
    return render(request, 'category_add.html', context)