from django.shortcuts import render,HttpResponse,redirect
from .models import Employee,Role,Department
from django.db.models import Q

def index(request):
    return render(request,'index.html')
def all_emp(request):
    emps=Employee.objects.all()
    context={'emps':emps}
    return render(request,'view_all_emp.html',context)
def add_emp(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        department = int(request.POST['department'])
        role =int( request.POST['role'])
        salary =int( request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phoneno =int( request.POST['phone.no'])
       # hireddate = int(request.POST['hireddate'])
        new_emp=Employee(first_name=firstname,last_name=lastname,dept_id=department,role_id=role,salary=salary,bonus=bonus,phone=phoneno)
        new_emp.save()
        return redirect('add_emp')
    elif request.method=="GET":
        return render(request,'add_emp.html')
def remove_emp(request , emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return redirect('remove_emp')
        except:
            return HttpResponse("Invalid id")
    emps=Employee.objects.all()
    context={'emps':emps}
    return render(request,'remove_emp.html' ,context)
def filter_emp(request):
    if request.method=='POST':
        name=request.POST["name"]
        department=request.POST["department"]
        role=request.POST["role"]
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) or Q(last_name__icontains=name))
        if department:
            emps=emps.filter(dept__name__icontains=department)
        if role:
            emps = emps.filter(role__name__icontains=role)
        context={'emps':emps}
        return render(request,'view_all_emp.html',context)
    elif request.method=="GET":
        return render(request, 'filter_emp.html')
