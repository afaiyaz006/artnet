from django.contrib.auth import views
from django.urls import path
from .views import ArtWorkCommentCreate,artStyleSubmitView
from .views import create_artwork_with_selected_style_view
from .views import home,profileview,create_artwork_view
from .views import signup,ArtWorkListView,ArtWorkDetailView
from .views import famousArtWorkCreation,ArtStyleDetailView
from .views import ProfileDetailView,ProfileListView,like_artwork
from .views import searchview
urlpatterns = [
    path('',home,name='home'),
]