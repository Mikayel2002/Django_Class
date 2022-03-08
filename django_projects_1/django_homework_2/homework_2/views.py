from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(requests):
    return HttpResponse("Hello World")
