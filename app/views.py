from django.shortcuts import render
from .forms import UserInputForm
from .knapsack import Optimizer


def index(request):
    form = UserInputForm()

    if request.method == 'POST':
        budget = float(request.POST.get('budget'))
        rating = float(request.POST.get('rating'))
        optimizer = Optimizer('kvdbeauty_data.csv')
        data = optimizer.optimize(budget=budget, 
          min_rating=rating)
        context = {
            'form': form,
            'cart': data['cart'],
            'total': data['total']
        }
        return render(request, "index.html", context)

    return render(request, "index.html", {"form": form})
