from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {})

my_list = ['name', 'age', 'password']
def about_view(request):
    context = {
        'my_list': my_list
    }
    return render(request, "about.html", context)
