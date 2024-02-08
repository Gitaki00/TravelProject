from django.http import HttpResponse
from django.shortcuts import render
from .models import place
# Create your views here.
def demo(request):
    obj=place.objects.all()
    context={
             'res':obj
             }
    return render(request,'index.html',context)
# def result(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,'result.html',{'res1':add,'res2':sub,'res3':mul,'res4':div,'n1':x,'n2':y})