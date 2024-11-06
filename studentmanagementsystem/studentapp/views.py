from django.shortcuts import render


from .forms import ContactForm
# Create your views here.

def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')

def skillspage(request):
    return render(request,'skills.html')

def projectpage(request):
    return render(request,'projects.html')

def contactpage(request):
    return render(request,'contact.html')