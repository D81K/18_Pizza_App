from django.shortcuts import render
from .forms import PizzaForm
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    form = PizzaForm()

    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order was successful')

    context = {
        'form': form,
    }
    return render(request, 'pizza/order.html', context)
