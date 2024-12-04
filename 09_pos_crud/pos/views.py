from django.shortcuts import render

# Create your views here.
def category_list(request):
    category1 = {
        'code': 'C001',
        'name' : 'Alat Berat'
    }

    context = {
        'title': 'List Category',
        'data1': 'Ini Data 1',
        'data2': 'Ini Data 2',
        'category1': category1,
    }
    return render(request, 'category_list.html', context)