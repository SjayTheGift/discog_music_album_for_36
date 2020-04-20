from django.urls import path

from .views import HomeView, SignUpView, LoginView, LogoutView, AlbumView, AlbumDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('login/', LoginView.as_view(), name='sign_in'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('albums/', AlbumView.as_view(), name='albums'),
    path('albums/detail/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
]
