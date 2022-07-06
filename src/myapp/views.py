from django.shortcuts import render
from django.views import View

# Create your views here.
class CourseView(View):

    context = {

    }
    def get(request, *args, **kwargs):
        return render(request, 'about.html',)