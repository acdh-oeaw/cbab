import requests
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from .forms import form_user_login
from .metadata import PROJECT_METADATA as PM
from copy import deepcopy


class AboutView(TemplateView):
    template_name = "webpage/about.html"


class StartView(TemplateView):
    template_name = "webpage/index.html"


class TermsOfUseView(TemplateView):
    template_name = "webpage/terms_of_use.html"


class ManualView(TemplateView):
    template_name = "webpage/manual.html"


class ImprintView(TemplateView):
    template_name = "webpage/imprint.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            imprint_url = f"{settings.ACDH_IMPRINT_URL}{settings.REDMINE_ID}"
        except Exception as e:
            context["imprint_body"] = e
            return context
        r = requests.get(imprint_url)
        if r.status_code == 200:
            context["imprint_body"] = f"{r.text}"
        else:
            context[
                "imprint_body"
            ] = """
            On of our services is currently not available.\
            Please try it later or write an email to\
            acdh-ch-helpdesk@oeaw.ac.at; if you are service provide,\
            make sure that you provided ACDH_IMPRINT_URL and REDMINE_ID
            """
        return context


#################################################################
#               views for login/logout                          #
#################################################################


def user_login(request):
    if request.method == "POST":
        form = form_user_login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", "/"))
            return HttpResponse("user does not exist")
    else:
        form = form_user_login()
        return render(request, "webpage/user_login.html", {"form": form})


def user_logout(request):
    logout(request)
    return render("webpage/user_logout.html")


#################################################################
#                    project info view                          #
#################################################################


def project_info(request):
    """
    returns a dict providing metadata about the current project
    """

    info_dict = deepcopy(PM)

    if request.user.is_authenticated:
        pass
    else:
        del info_dict["matomo_id"]
        del info_dict["matomo_url"]
    info_dict["base_tech"] = "django"
    info_dict["framework"] = "djangobaseproject"
    return JsonResponse(info_dict)
