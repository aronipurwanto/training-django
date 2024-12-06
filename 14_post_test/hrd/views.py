from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department
from .forms import EmployeeForm, DepartmentForm

def logout_view(request):
    logout(request)
    return redirect('login') # Redirect ke halaman login setelah logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee_list')  # Ganti dengan URL yang diinginkan setelah login
        else:
            return render(request, 'login.html', {'form': {}})
    else:
        return render(request, 'login.html', {'form': {}})

@login_required(login_url='login')
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

@login_required(login_url='login')
def create_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'create_department.html', {'form': form})

@login_required(login_url='login')
def update_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'update_department.html', {'form': form, 'department': department})

@login_required(login_url='login')
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'delete_department.html', {'department': department})

@login_required(login_url='login')
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

@login_required(login_url='login')
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'create_employee.html', {'form': form})