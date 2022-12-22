from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Priyanka. This is after the change")
# Create your views here.
