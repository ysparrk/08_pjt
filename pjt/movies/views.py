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


# @require_safe
def recommended(request, genre_pk):
    
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    context = {
        'genres' : genres,
        'movies' : movies,
    }
    return render(request, 'movies/recommended.html', context)
    



    # for movie in movies:
    #     movie.


    # movie_list = sorted(movie_list, key = lambda x: (-x[1], -x[2]))

    # context = {
    #     'movie_list' : movie_list,
    # }

    # print(movie_list)
    # context = {
    #     'genres' : genres,
    #     'movies' : movies,

    # }
    
    # return render(request, 'movies/recommended.html', context)