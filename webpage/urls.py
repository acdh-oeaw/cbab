from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start_view, name="start"),
    url(r'^imprint/$', views.imprint_view, name='imprint'),
    url(r'^accounts/login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
]
