from django.urls import path
from . import views  # Required relative import statement

# movies/: Root URL
# movies/1/details: Id #1 & details

# URL Configuration:
urlpatterns = [
    # root Url, You are not calling just passing a reference.
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.details, name='movies_detail')
]
