from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def get_recipe(request, dish):
    persons_number = int(request.GET.get('servings', 1))
    context = {'recipe':{}}
    for ingredient, quantity in DATA[dish].items():
        context['recipe'][ingredient] = quantity * persons_number
    return context

def get_omlet_recipe(request):
    context = get_recipe(request, 'omlet')+
    return render(request, 'calculator/index.html', context)

def get_pasta_recipe(request):
    context = get_recipe(request, 'pasta')
    return render(request, 'calculator/index.html', context)

def get_buter_recipe(request):
    context = get_recipe(request, 'buter')
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:

