from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    html = "<html><body>Hi, Django</body></html>"
    return HttpResponse(html)

def welcome(request):
    html = "<html><body>Welcome to Django.</body></html>"
    return HttpResponse(html)

def template_test(request):
    return render(request, 'test.html')









