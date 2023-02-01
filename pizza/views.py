from django.shortcuts import render
from .forms import PizzaForm
from django.contrib import messages
from .models import Pizza


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    form = PizzaForm()

    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            pizza_id = pizza.id
            messages.success(request, 'Order is successful!!!')
        else:
            messages.warning(request, 'Something wrong!!!')
            pizza_id = None
        return render(request, 'pizza/order.html', {'form':form, 'pizza_id':pizza_id})

    context = {
        'form':form,
    }
    return render(request, 'pizza/order.html', context)


def update_pizza(request, id):
    pizza = Pizza.objects.get(id=id)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated!!')
        else:
            messages.error(request, 'Something wrong!!')
        
    return render(request, 'pizza/update_pizza.html', {'form':form})