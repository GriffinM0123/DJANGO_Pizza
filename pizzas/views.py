from django.shortcuts import render, redirect

from .forms import ToppingForm
from .models import Pizza

# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()


    context = {'pizzas':pizzas}

    return render(request,'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = pizza.topping_set.all()

    context = {'pizza':pizza,'toppings':toppings}

    return render(request, 'pizzas/pizza.html', context)

def new_topping(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)

        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)
        
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_topping.html', context)







