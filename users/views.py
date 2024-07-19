from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreationForm


class SignUpView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('weather:index')
    template_name = 'users/signup.html'
