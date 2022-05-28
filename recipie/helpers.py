from recipie.models import Recipie
from recipie.models import Recipie, RecipieIngredient, Ingredient
Recipie

def create_recipie_ingredient(ingredient, recipie):
    _ing = Ingredient.objects.get(id=ingredient.get('ingredient').get('id'))

    extra = {
        'amount': ingredient.get('amount', None),
        'replaces': ingredient.get('replaces', None),
        'replaces_reason': ingredient.get('replaces_reason', None)
    }

    RecipieIngredient.objects.create(
        recipie= recipie,
        ingredient = _ing,
        **extra
    )

def remove_old_recipie_ingredients(ingredients, saved_ingredients):
    item_ids = [item.get('id', None) for item in ingredients]
    item_ids = filter(None,item_ids)

    items_to_remove = saved_ingredients.exclude(pk__in=item_ids)
    for item in items_to_remove:
        item.delete()


def update_recipie_ingredient(ingredient, recipie,):
    id = ingredient.get('id', None)
    print(ingredient)
    if(id is not None):
        RecipieIngredient.objects.filter(recipie=recipie, id=id).update(
            amount=ingredient.get('amount', None),
            replaces=ingredient.get('replaces', None),
            replaces_reason=ingredient.get('replaces_reason', None),
            ingredient=ingredient.get('ingredient').get('id')
        )