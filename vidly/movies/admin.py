from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    # field attribute specify the fields we want to show in our form:
    #fields = ('title', 'genre')
    # or
    # exclude attribute specfies the fields we want to exclude
    # add coma if only one field if not python will think its a string wrapped in parentesis
    exclude = ('date_created',)
    list_display = ('title', "number_in_stock", "daily_rate")


    # Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
