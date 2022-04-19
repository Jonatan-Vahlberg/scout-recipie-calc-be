

from dataclasses import fields
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model # If used custom user model
from models import Cart, CartRecipie, PortionGroup
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


class CartRecipieSerializer(serializers.ModelSerializer):
    recipie = serializers.ReadOnlyField(source="recipie")

    class Meta:
        model = CartRecipie
        fields = ('recipie')

class PortionGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortionGroup
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):

    recipies = CartRecipieSerializer(many=True, read_only=True)
    portions = PortionGroupSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ('id','updated_at','recipies')