from django.urls import re_path
from . import views

app_name = "places"


urlpatterns = [
    re_path(r"^$", views.PlaceListView.as_view(), name="place_list"),
    re_path(r"^create/$", views.create_place, name="place_create"),
    re_path(r"^edit/(?P<pk>[0-9]+)$", views.edit_place, name="place_edit"),
    re_path(
        r"^delete/(?P<pk>[0-9]+)$", views.PlaceDelete.as_view(), name="place_delete"
    ),
]
