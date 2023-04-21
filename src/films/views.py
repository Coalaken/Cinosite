from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Film, UserFilmRelation
from .forms import FilmAddForm
from .services import change_bookmarks, like


@login_required(login_url="/login")
def home(request):
    if request.method == 'POST':
        film_name = request.POST.get("film-name")

        if film_name:
            change_bookmarks(request, Film, UserFilmRelation, film_name)


    films = Film.objects.select_related('added_by').all()
    data = {
        'films': films
    }
    return render(request, 'films/home.html', data)
    
    
@login_required(login_url="/login")
def search(request):    
    if request.method == 'POST':
        change_bookmarks(request, Film, UserFilmRelation)
    films = Film.objects.select_related('added_by').\
        filter(name__icontains=request.GET.get("search"))
    data = {
        'films': films
    }
    return render(request, 'films/home.html', data)
    

@login_required(login_url="/login")
@permission_required("films.can_add_film")
def add_film(request):
    if request.method == "POST":
        form = FilmAddForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.added_by = request.user
            form.save(commit=True)
        else:
            form = FilmAddForm()
            return render(request, 'films/add_film.html', {'form': form})
    elif request.method == 'GET':
        form = FilmAddForm()
        return render(request, 'films/add_film.html', {'form': form})
        
        
@login_required(login_url='/login') 
def bookmarks(request):
    if request.method == 'POST':
        change_bookmarks(request, Film, UserFilmRelation)
    films = Film.objects.select_related('added_by').\
        filter(userfilmrelation__user=request.user, userfilmrelation__in_bookmarks=True)
    data = {
        'films': films
    }
    return render(request, 'films/home.html', data)


@login_required(login_url="/login")
def film_page(request, pk):
    if request.method == 'POST':
        film_liked = request.POST.get("film-liked")
        if film_liked:
            like(request, Film, UserFilmRelation, film_liked)
    film = get_object_or_404(Film, pk=pk)
    data = {
        'film': film
    }
    return render(request, 'films/film_page.html', data)