from django.shortcuts import render


def home(request):
    return render(request, 'Home/index.html')


def contact(request):
    return render(request, 'Home/contactus.html')
