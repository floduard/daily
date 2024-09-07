from django.shortcuts import HttpResponse, render

def home(request):
    return render(request, 'app/home.html')
