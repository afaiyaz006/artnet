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
    path('signup',signup,name='signup'),
    path('profile',profileview,name='profile'),
    path('create_artwork',create_artwork_view,name='create_artwork'),
    path('create_artwork_with_artstyle',create_artwork_with_selected_style_view,name='create_artwork_artstyle'),
    path('create_artwork_with_famous_artstyle',famousArtWorkCreation,name='create_artwork_famous_artstyle'),
    path('submit_artstyle',artStyleSubmitView,name='submit_artstyle'),
    path('artworks/',ArtWorkListView.as_view(),name='artworks'),
    path('artworks/<int:pk>',ArtWorkDetailView.as_view(),name='artwork-detail'),
    path('artstyles/<int:pk>',ArtStyleDetailView.as_view(),name='artstyle-detail'),
    path('artworks/<int:pk>/comment',ArtWorkCommentCreate.as_view(),name='artwork-comment'),
    path('users/<int:pk>',ProfileDetailView.as_view(),name='user-details'),
    path('users',ProfileListView.as_view(),name='user-list'),
    path('like/<int:id>',like_artwork,name='like_artwork'),
    path('search',searchview,name='search'),
]