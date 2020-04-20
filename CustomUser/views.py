from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class SignUpView(generic.TemplateView):
    template_name = 'sign_up.html'


class LoginView(generic.TemplateView):
    template_name = 'sign_in.html'


class LogoutView(generic.TemplateView):
    template_name = 'logout.html'


class AlbumView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/login/'
    template_name = 'albums.html'


class AlbumDetailView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/login/'
    template_name = 'album_detail.html'
