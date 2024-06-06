from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

favicon_view = RedirectView.as_view(url="/static/favicon.ico", permanent=True)

urlpatterns = [
    url(r"^$", views.StartView.as_view(), name="start"),
    url(r"^favicon\.ico$", favicon_view),
    url(r"^imprint/$", views.ImprintView.as_view(), name="imprint"),
    url(r"^project-info/$", views.project_info, name="project_info"),
    url(r"^terms-of-use/$", views.TermsOfUseView.as_view(), name="terms-of-use"),
    url(r"^about/$", views.AboutView.as_view(), name="about"),
    url(r"^manual/$", views.ManualView.as_view(), name="manual"),
    url(r"^accounts/login/$", views.user_login, name="user_login"),
    url(r"^logout/$", views.user_logout, name="user_logout"),
]
