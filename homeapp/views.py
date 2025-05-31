from django.shortcuts import render

def home_view(request):
    return render(request, 'homeapp/home.html')

def about_view(request):
    return render(request, 'homeapp/about.html')

def portfolio_view(request):
    return render(request, 'homeapp/portfolio.html')

def blog_view(request):
    return render(request, 'homeapp/blog.html')

def contact_view(request):
    return render(request, 'homeapp/contact.html')
