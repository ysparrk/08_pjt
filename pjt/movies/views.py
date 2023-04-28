from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie, Genre


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()    
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    
    genres = Genre.objects.all()
    movies = Movie.objects.all()

    context = {
        'genres' : genres,
        'movies' : movies,
    }
    return render(request, 'movies/recommended.html', context)
    
@require_safe
def genre_recommended(request, genre_pk):
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    movie_list = []

    for movie in movies:
        
        m = movie.genres.values()
        for i in m:
            if i['id'] == genre_pk:
                movie_list.append(movie)

    context = {
        'genres' : genres,
        'movie_list' : movie_list,
    }
    return render(request, 'movies/recommended.html', context)
