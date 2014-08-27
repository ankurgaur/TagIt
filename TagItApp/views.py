from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("login")

def signup(request):
    return HttpResponse("signup")

