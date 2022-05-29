from django.urls import re_path
from rest_framework import authtoken
from . import views

urlpatterns = [
    re_path(
        r'^recipies/$',
        views.RecipieListView.as_view(),
        name="recipie_list_view"
    ),
    re_path(
        r'^recipies/(?P<pk>[0-9]+)/$',
        views.RecipieDetailView.as_view(),
        name="recipie_detail_view"
    ),
    re_path(
        r'^ingredients/$',
        views.IngredientListView.as_view(),
        name="ingredient_list_view"
    )
    ,re_path(
        r'^user/create/$',
        views.CreateUserView.as_view(),
        name="Create new User"
    )
    ,re_path(
        r'^user/$',
        views.GetUserView.as_view(),
        name="Get User"
    ),

    re_path(
        r'^cart/$',
        views.CreateCartView.as_view(),
        name="Create cart view",
    ),
    re_path(
        r'^user/cart/$',
        views.RetriveUserCartView.as_view(),
        name="User Cart retrive view",
    ),

    re_path(
        r'^user/cart/(?P<pk>[0-9]+)/$',
        views.UpdateUserCartView.as_view(),
        name="Cart update view",
    )
]
