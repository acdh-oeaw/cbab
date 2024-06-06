from django.urls import re_path
from . import views

app_name = "bib"

urlpatterns = [
    re_path(r"^synczotero/$", views.sync_zotero, name="synczotero"),
    re_path(r"^synczotero/result$", views.sync_zotero_action, name="synczotero_action"),
]
