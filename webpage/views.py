from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import form_user_login
from .metadata import PROJECT_METADATA as PM


def start_view(request):
    if PM is not None:
        context = {"metadata": PM}
    else:
        context = {}

    return render(request, 'webpage/index.html', context)


def imprint_view(request):
    if PM is not None:
        context = {"metadata": PM}
    else:
        context = {}

    return render(request, 'webpage/imprint.html', context)


#################################################################
#               views for login/logout                          #
#################################################################

def user_login(request):
    if request.method == 'POST':
        form = form_user_login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(request.GET.get('next', '/'))
                else:
                    return HttpResponse('not active.')
            else:
                return HttpResponse('user does not exist')
    else:
        form = form_user_login()
        return render(request, 'webpage/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render_to_response('webpage/user_logout.html')
