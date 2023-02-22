from django.shortcuts import render
from .models import EmployeeData
# Create your views here.

def home(request):
    Employee = EmployeeData.objects.all()
    data = {
        'Employee':Employee
            }
    return render(request,'my_webapp/home.html', data)