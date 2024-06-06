from django.shortcuts import render, render_to_response
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


class ImprintView(TemplateView):
    template_name = "webpage/imprint.html"


class TermsOfUseView(TemplateView):
    template_name = "webpage/terms_of_use.html"


class ManualView(TemplateView):
    template_name = "webpage/manual.html"


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
    return render_to_response("webpage/user_logout.html")


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
