from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('<h1>Hello There</h1><p>This is cool.</p>')
