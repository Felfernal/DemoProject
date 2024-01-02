from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return HttpResponse("This is the abouts page!")


def contact(request):
    name = "Hello User!"
    return render(request, "contacts.html", {'obj': name})


def details(request):
    return render(request, "details.html")


def thanks(request):
    return HttpResponse("Thank you for your time!")


def result(request):
    a = int(request.GET["num1"])
    b = int(request.GET["num2"])
    add = a + b
    sub = a-b
    prod = a*b
    div = a/b
    return render(request, "result.html", {'sum': add, 'sub': sub, 'prod': prod, 'div': div, 'n1': a, 'n2': b})
