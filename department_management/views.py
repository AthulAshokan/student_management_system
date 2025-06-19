from django.shortcuts import render

def departments(request):
    return render(request, 'departments_only.html')

def exlore(request):
    return render(request, 'explore.html')

