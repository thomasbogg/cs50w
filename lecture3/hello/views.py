from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# we should think of each view as something the user might want to see
def index(request):
    return render(request, 'hello/index.html')

def thomas(request):
    return HttpResponse('Hello, Thomas!')

def greet(request, name):
    return render(request, 'hello/greet.html',{
    'name': name.capitalize()
    })
