from django.shortcuts import redirect, render

def homepage(request):
    return render(request, 'home.html')

def workHistory(request):
    return render(request, 'work-history.html')
