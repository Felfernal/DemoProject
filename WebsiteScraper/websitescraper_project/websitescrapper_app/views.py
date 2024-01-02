from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests

from .models import Links


# Create your views here.
def home(request):
    if request.method == 'POST':
        link_new = request.POST.get('page')
        urls = requests.get(link_new)
        bsoup = BeautifulSoup(urls.text, 'html.parser')

        for link in bsoup.find_all('a'):
            li_address = link.get('href')
            li_name = link.string
            Links.objects.create(address=li_address, strname=li_name)
        return HttpResponseRedirect('/')
    else:

        data_values = Links.objects.all()

    return render(request, 'home.html', {'data': data_values})


def clear(request):
    links = Links.objects.all()
    if request.method == 'POST':
        links.delete()
        return redirect('/')
    return render(request, 'clear.html')
