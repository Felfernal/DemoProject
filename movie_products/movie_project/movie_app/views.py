from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies
from .forms import Movie_Form


# Create your views here.

def index(request):
    movie = Movies.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, "index.html", context)


def detail(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movie})


def add(request):
    if request.method == 'POST':
        mov_name = request.POST.get('name')
        mov_desc = request.POST.get('desc')
        mov_year = request.POST.get('year')
        mov_genre = request.POST.get('genre')
        mov_img = request.FILES['img']
        movie = Movies(name=mov_name, desc=mov_desc, year=mov_year, genre=mov_genre, img=mov_img)
        movie.save()
    return render(request, 'add.html')


def update(request, id):
    movie = Movies.objects.get(id=id)
    form = Movie_Form(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
