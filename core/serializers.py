


from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from core.helpers import create_cart_item, remove_old_cart_items, update_cart_item

from recipie.models import Recipie # If used custom user model
from .models import Cart, CartItem, PortionGroup
from recipie.serializers import RecipieSerializer
UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", )

class UserRegisterSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, user):
        token = RefreshToken.for_user(user)
        refresh = str(token)
        access = str(token.access_token)
        return {
            "refresh": refresh,
            "access": access,
        }

    class Meta:
        model = UserModel
        fields = ('id', 'password', 'username', 'token')
    
    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user


class PortionGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortionGroup
        fields = (
            'xs',
            'sm',
            'md',
            'lg',
            'xl',

            'VEGITARIAN',
            'VEGAN',
            'DAIRY',
            'MP_ALLERGIES',
            'GLUTEN',
            'LEGUMINOUS',
        )

class CartItemSerializer(serializers.ModelSerializer):
    recipie = RecipieSerializer()
    portions = PortionGroupSerializer()
    id = serializers.ModelField(model_field=CartItem()._meta.get_field('id'), required=False)

    class Meta:
        model = CartItem
        fields = ('id', 'recipie', 'portions')


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'updated_at', 'items','user')
    
    def create(self, validated_data):
        items = validated_data.pop('items')
        cart = Cart.objects.create(**validated_data)
        for item in items:
            create_cart_item(item, cart)
    
        return cart

    def update(self, instance, validated_data):
        items = validated_data.pop('items')
        saved_items = instance.items.all()
        remove_old_cart_items(items, saved_items)
        for item in items:
            _item = saved_items.filter(id=item.get('id'),)
            if not _item.exists():
                create_cart_item(item, instance)
            else:
                update_cart_item(_item, item, saved_items)
                
        instance = super().update(instance, validated_data)
        return instance