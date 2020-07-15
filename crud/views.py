from django.shortcuts import render
from django.http import HttpResponse
def about(request):
   return render(request, 'about.html')
def blog_single(request):
    return render(request, 'blog_single.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request, 'index.html')
def job_listings(request):
    return render(request, 'job_listings.html')
def job_single(request):
    return render(request, 'job_single.html')
def services(request):
    return render(request, 'services.html')

