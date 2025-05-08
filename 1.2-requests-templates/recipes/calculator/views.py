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
}


def calculate_ingredients(request, dish):
    template_name = 'calculator/index.html'

    try:
        servings = int(request.GET.get('servings', 1))
    except ValueError:
        servings = 1

    base_recipe = DATA.get(dish)
    if base_recipe is None:
        return render(request, 'calculator/error.html', {'message': 'Рецепт не найден.'})

    recipe = {key: value * servings for key, value in base_recipe.items()}
    context = {'recipe': recipe}
    return render(request, template_name, context)
