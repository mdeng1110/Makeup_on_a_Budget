from django.shortcuts import render
from .forms import UserInputForm


def index(request):
    form = UserInputForm()
    return render(request, "index.html", {"form": form})
