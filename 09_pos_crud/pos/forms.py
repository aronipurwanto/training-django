from django import forms

from pos.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['code','name']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }