from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(
        request,
        'single_pages/medi.html'
    )

def qqq(request):
    return render(
        request,
        'single_pages/qqq.html'
    )

def searchhospital(request):
    return render(
        request,
        'single_pages/searchhospital.html'
    )

def search_hospital_seoul(request):
    return render(
        request,
        'single_pages/search_hospital_seoul.html'
    )

def search_hospital_incheon(request):
    return render(
        request,
        'single_pages/search_hospital_incheon.html'
    )

def search_hospital_busan(request):
    return render(
        request,
        'single_pages/search_hospital_busan.html'
    )

def self(request):
    return render(
        request,
        'single_pages/self.html'
    )

def post_one_list(request):
    return render(
        request,
        'single_pages/post_one_list.html'
    )

def post_one_list2(request):
    return render(
        request,
        'single_pages/post_one_list2.html'
    )