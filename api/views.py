from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, pagination, filters, status
from rest_framework.response import Response
from recipie.serializers import RecipieSerializer, IngredientSerializer
from recipie.models import Recipie, Ingredient, RecipieIngredient
from operator import itemgetter

class SmallPaginationSet(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

class StandardPaginationSet(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20

class LargePaginationSet(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class StandardSearchInterface():
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)

# Create your views here.
class RecipieListView(StandardSearchInterface, generics.ListCreateAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializer
    pagination_class = StandardPaginationSet
    search_fields= ['name']

    def create(self, request, *args, **kwargs):
        ingredients = request.data.get('ingredients')
        response = super().create(request, *args, **kwargs)
        response_id = response.data.get('id')
        if(response_id is not None):
            for ingredient in ingredients:
                _ing = Ingredient.objects.get(id=ingredient.get('ingredient_id'))
                _rec = Recipie.objects.get(id=response_id)

                amount, replaces = itemgetter('amount','replaces')(ingredient)
                print(amount)
                extra = {}
                if amount is not None:
                    extra['amount'] = amount
                if replaces is not None:
                    extra['replaces'] = replaces
                    extra['replaces_reason'] = ingredient.get('replaces_reason')
                RecipieIngredient.objects.create(
                    recipie= _rec,
                    ingredient = _ing,
                    **extra

                )


        return response


class RecipieDetailView(generics.RetrieveAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializer

class IngredientListView(StandardSearchInterface, generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = LargePaginationSet

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data, many=isinstance(data, list))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    