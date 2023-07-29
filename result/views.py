from django.shortcuts import render
from .result import get_number
from django.core.paginator import Paginator
from .models import Student

def rank(request):
    objects = Student.objects.order_by('-number')
    p = Paginator(objects,1000)
    page = request.GET.get("page")
    students = p.get_page(page)
    r = (students.number-1)*1000
    return render(request,'index.html',{
        'students':students,
        'r':r
    })

def entry(start,end):
    for i in range(start,end+1):
        print(i)
        num = get_number(i)
        if num['name'] == None:
            continue
        if num['grp'] == 'SCIENCE':
            Student.objects.create(
                name=num['name'],
                school=num['schl'],
                roll=i,
                number=num['total'],
                gpa=num['gpa']
            )#133234