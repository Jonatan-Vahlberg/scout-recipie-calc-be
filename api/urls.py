from django.urls import re_path
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
    )
]
