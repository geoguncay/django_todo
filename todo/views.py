""" Views for todo app"""
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    """Home page view"""
    return render(request, "task.html")


def create_task(request):
    """Create task view"""
    print(request.POST)
    redirect(home)
    return render(request, "task.html")
