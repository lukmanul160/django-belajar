from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def index(request):
    return HttpResponse("<h1>HOME</h1>")

def angka(request,input):
    heading = "<h1>Page Angka </h1>"
    str = heading + input
    return HttpResponse(str)