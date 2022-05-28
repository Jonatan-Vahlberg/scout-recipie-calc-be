
from rest_framework import generics, pagination, filters, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.serializers import CartSerializer, UserSerializer, UserRegisterSerializer
from recipie.serializers import RecipieSerializer, IngredientSerializer
from recipie.models import Recipie, Ingredient
from core.models import Cart
from django.contrib.auth import get_user_model

### ABSTRACT VIEWS ###

class UnauthenticatedRequest():
    permission_classes = [AllowAny]

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

### RECIPIE VIEWS ###

class RecipieListView(StandardSearchInterface, UnauthenticatedRequest, generics.ListCreateAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializer
    pagination_class = StandardPaginationSet
    search_fields= ['name']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()       
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipieDetailView(UnauthenticatedRequest, generics.RetrieveUpdateAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializer

class IngredientListView(StandardSearchInterface, UnauthenticatedRequest, generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = LargePaginationSet


    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data, many=isinstance(data, list))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


### CORE VIEWS ###

class CreateUserView(UnauthenticatedRequest, generics.CreateAPIView):
    model = get_user_model
    serializer_class = UserRegisterSerializer
    
class GetUserView(generics.RetrieveAPIView):
    model = get_user_model
    serializer_class = UserSerializer

    def get(self, request, format=None):
        # TODO: only allow get for own user
        serializer = self.get_serializer(request.user)

        return Response(serializer.data)

class CreateCartView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        data = {
            **request.data,
            'user': request.user.id
        }
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
           
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetriveUpdateUserCartView(generics.RetrieveUpdateAPIView):
    model = Cart
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)