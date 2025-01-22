from django.shortcuts import render
from django.http import HttpResponse

def home(requet):
    return HttpResponse("This is first Project")