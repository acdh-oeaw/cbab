from django.urls import re_path
from django.views.generic.base import RedirectView
from . import views

app_name = 'webpage'

favicon_view = RedirectView.as_view(url="/static/favicon.ico", permanent=True)

urlpatterns = [
    re_path(r"^$", views.StartView.as_view(), name="start"),
    re_path(r"^favicon\.ico$", favicon_view),
    re_path(r"^imprint/$", views.ImprintView.as_view(), name="imprint"),
    re_path(r"^project-info/$", views.project_info, name="project_info"),
    re_path(r"^terms-of-use/$", views.TermsOfUseView.as_view(), name="terms-of-use"),
    re_path(r"^about/$", views.AboutView.as_view(), name="about"),
    re_path(r"^manual/$", views.ManualView.as_view(), name="manual"),
    re_path(r"^accounts/login/$", views.user_login, name="user_login"),
    re_path(r"^logout/$", views.user_logout, name="user_logout"),
]
