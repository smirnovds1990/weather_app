from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreationForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class SignUpView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('index')
    template_name = 'users/signup.html'
