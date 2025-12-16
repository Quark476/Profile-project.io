from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def services(request):
    return render(request, 'main/services.html')

def aboutus(request):
    return render(request, 'main/aboutus.html')