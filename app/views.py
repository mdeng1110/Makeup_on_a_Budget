from django.shortcuts import render
from .forms import UserInputForm


def index(request):
    return render(request, 'index.html', {})

def get_user_input(request):
    form = UserInputForm()
    return render(request, "index.html", {"form": form})