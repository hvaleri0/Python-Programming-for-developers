from django.urls import path
from . import views  # Required relative import statement

# movies/: Root URL
# movies/1/details: Id #1 & details

# URL Configuration:

app_name = 'movies'
urlpatterns = [
    # root Url, You are not calling just passing a reference.
    # no need to namespace eg. name=''movies_index, now you have app_name defined:
    path('', views.index, name='index'),
    path('<int:movie_id>', views.details, name='detail')
]
