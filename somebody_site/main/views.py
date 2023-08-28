from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, template_name='home.html')


def page1(request):
    dict_post = {
        "fname": request.POST["fname"],
        "lname": request.POST["lname"],
        "pas": request.POST["pas"],
    }
    return render(request, template_name='page1.html', context=dict_post)


def page2(request, slug=None):

    return render(request, template_name='page2.html', context={"slug": slug})









