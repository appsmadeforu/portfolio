from django.shortcuts import render

from django.http import HttpResponse


def base(request):
    return render(request, 'base.html')
# Create your views here.

def newnew(request):
    pass
