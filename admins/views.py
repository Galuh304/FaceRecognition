from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'dashboard.html')

def attendance(request):
    return render(request, 'attendance.html')

def user(request):
    return render(request, 'user.html')