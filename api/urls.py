from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('suggestions/', views.suggestions, name='suggestions'),
    path('home/', views.home, name='home'),
    path('artist/', views.artist, name='artist'),
    path('artist_albums/', views.artist_albums, name='artist_albums'),
    path('album/', views.album, name='album'),
    path('album_browse_id/', views.album_browse_id, name='album_browse_id'),
    path('user/', views.user, name='user'),
    path('song_related/', views.song_related, name='song_related'),
    path('lyrics/', views.lyrics, name='lyrics'),
    path('tasteprofile/', views.tasteprofile, name='tasteprofile'),
    path('mood-categories/', views.mood_categories, name='mood_categories'),
    path('mood-playlists/', views.mood_playlists, name='mood_playlists'),
]
