from django.urls import re_path
from . import views

app_name = "browsing"

urlpatterns = [
    re_path(
        r"burialsites/$", views.BurialSiteListView.as_view(), name="browse_burialsites"
    ),
    re_path(
        r"burialgroups/$",
        views.BurialGroupListView.as_view(),
        name="browse_burialgroups",
    ),
    re_path(r"burials/$", views.BurialListView.as_view(), name="browse_burials"),
    re_path(r"urncovers/$", views.UrnCoverListView.as_view(), name="browse_urncovers"),
    re_path(r"urns/$", views.UrnListView.as_view(), name="browse_urns"),
    re_path(r"gravegoods/$", views.GraveGoodListView.as_view(), name="browse_gravegoods"),
    re_path(
        r"gravegoodsother/$",
        views.GraveGoodOtherListView.as_view(),
        name="browse_gravegoodsother",
    ),
    re_path(
        r"deadbodyremains/$",
        views.DeadBodyRemainsListView.as_view(),
        name="browse_deadbodyremains",
    ),
    re_path(
        r"animalremains/$",
        views.AnimalRemainsListView.as_view(),
        name="browse_animalremains",
    ),
    re_path(r"all/$", views.MainListView.as_view(), name="browse_all"),
    re_path(
        r"download-results/$",
        views.MainListDownloadView.as_view(),
        name="download-results",
    ),
]
