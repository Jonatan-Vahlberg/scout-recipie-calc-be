
from recipie.models import Recipie
from core.models import CartItem, PortionGroup
Recipie
def create_cart_item(item, cart):
    portions = item.pop('portions')
    item_recipie = item.pop('recipie')
    recipie_id = item_recipie.get('id')
    recipie = Recipie.objects.get(id=recipie_id)
    cart_item = CartItem.objects.create(cart=cart, recipie=recipie)
    PortionGroup.objects.create(cart_item=cart_item, **portions)

def remove_old_cart_items(items, saved_items):
    item_ids = [item.get('id', None) for item in items]
    item_ids = filter(None,item_ids)

    items_to_remove = saved_items.exclude(pk__in=item_ids)
    for item in items_to_remove:

        item.delete()


def update_cart_item(instance_item, item, saved_items,):
    id = item.get('id', None)
    instance_item = saved_items.get(id=id)
    PortionGroup.objects.filter(cart_item=instance_item).update(**item.get('portions'))