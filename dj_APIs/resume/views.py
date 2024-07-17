from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def projects(request):
    return render(request, "projects.html")

def experiences(request):
    experience=[
        {"company": "abc",
         "position": "python developer"},
        {"company": "abc",
         "position": "python developer"},
         {"company": "abc",
         "position": "python developer"},
    ]
    return render(request, "experiences.html", {"experience":experience})