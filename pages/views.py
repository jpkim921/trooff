# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page_view(request, *args, **kwargs):
    return render(request, "pages/home_page.html", {})

def contact_page_view(request, *args, **kwargs):
    return render(request, "pages/contact_page.html", {})
