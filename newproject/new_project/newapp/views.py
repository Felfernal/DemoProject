from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Genre
from .models import Most_Played


# Create your views here.
def login(request):
    if request.method == 'POST':
        username1 = request.POST['Username']
        password1 = request.POST['pwd']
        user = auth.authenticate(username=username1, password=password1)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Username or Password is incorrect")
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def demo(request):
    obj = Genre.objects.all()
    obj1 = Most_Played.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})



def register(request):
    if request.method == 'POST':
        usernm = request.POST['Username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        mail = request.POST['mail']
        password = request.POST['pwd']
        password1 = request.POST['pwd1']

        if password == password1:
            if User.objects.filter(username=usernm).exists():
                messages.info(request, "Username already in use. Please select a different one.")
                return redirect('registration')
            elif User.objects.filter(email=mail).exists():
                messages.info(request, "This mail is already registered.")
                return redirect('registration')
            else:
                user = User.objects.create_user(username=usernm, password=password, first_name=fname, last_name=lname,
                                                email=mail)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "Passwords doesn't match")
            return redirect('registration')

    return render(request, 'register.html')
# def about(request):
#     return render(request, "about.html")
#
#
# def contact(request):
#     return HttpResponse("This is the contacts page!")
