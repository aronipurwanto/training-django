from django import forms
from .models import Employee, Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'date_of_birth': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'place_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'religion': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'  # Atau ['code', 'name'] jika ingin spesifik
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }