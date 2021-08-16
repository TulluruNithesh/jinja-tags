from os import name
from django.shortcuts import render

# Create your views here.
def hai(request):
    return render(request,'hai.html',context={'name':'nikky','age':23})


def hello(request):
    return render(request,'hello.html',context={'name':'ramsagar','age':27})
