from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    # Select all the item in the table - # Select * FROM movies_movie:
    movies = Movie.objects.all()

    # Filter Items in the table - Select * FROM movies_movie WHERE release_year=1984:
    # Movie.objects.filter(release_year=1984)

    # Get one Item in the table - Select * FROM movies_movie WHERE ...:
    # Movie.objects.get(id=1)

    # output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)

    return render(request, 'movies/index.html', {'movies': movies})


def details(request, movie_id):
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()

    # easier implentation with django shortcuts:
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
