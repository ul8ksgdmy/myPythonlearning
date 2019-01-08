from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h2 style="color:red">회원가입입니다.</h2>')