from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def qqq(request):
    return render(
        request,
        'single_pages/qqq.html'
    )

def self(request):
    return render(
        request,
        'single_pages/self.html'
    )