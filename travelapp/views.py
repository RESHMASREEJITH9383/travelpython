from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from .models import place
def demo(request):
    obj=place.objects.all()
    return render (request,'index.html',{"obj":obj})
