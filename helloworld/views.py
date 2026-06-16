from django.shortcuts import render

def homepageview(request):
     return render(request, 'home.html')

def aboutusview(request):
     return render(request, 'about.html')

def contactusview(request):
     return render(request, 'contact.html')