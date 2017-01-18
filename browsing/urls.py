from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'burialsites/$', views.BurialSiteListView.as_view(), name='browse_burialsites'),
    url(r'burialgroups/$', views.BurialGroupListView.as_view(), name='browse_burialgroups'),
    url(r'burials/$', views.BurialListView.as_view(), name='browse_burials'),
    url(r'urncovers/$', views.UrnCoverListView.as_view(), name='browse_urncovers'),
    url(r'urns/$', views.UrnListView.as_view(), name='browse_urns'),
    url(r'gravegoods/$', views.GraveGoodListView.as_view(), name='browse_gravegoods'),
    url(r'gravegoodsother/$', views.GraveGoodOtherListView.as_view(), name='browse_gravegoodsother'),
    url(r'deadbodyremains/$', views.DeadBodyRemainsListView.as_view(), name='browse_deadbodyremains'),
    url(r'animalremains/$', views.AnimalRemainsListView.as_view(), name='browse_animalremains'),
]
