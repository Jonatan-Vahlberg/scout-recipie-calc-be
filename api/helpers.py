from core.models import CartItem, Cart, PortionGroup
from recipie.models import Recipie


def update_and_remove_cart_items(items, cart, instance):
    """
    Update a list by removing all items in a second list.
    """
    
    filtered =  instance.items.all()

    print(filtered)
    if items:
        if filtered:
            for item in filtered:
                if not item in items:
                    instance.items.remove(item)
        for item_to_add in items:
            if not item_to_add in filtered:
                recipie_id = item_to_add.get('recipie').get('id')
                recipie = Recipie.objects.get(id=recipie_id)
                cart_item = CartItem.objects.create(cart=cart,
                    recipie=recipie,
                )
                PortionGroup.objects.create(cart_item=cart_item, **item_to_add.get('portions'))
                instance.items.add(cart_item)
    
    return instance.items.all()
