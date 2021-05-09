from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
        request,
        'single_pages/index.html'
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