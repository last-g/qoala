from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import TokenAuthForm
from .models import Team

# Create your views here.


def show(req, name):
    team = get_object_or_404(Team, name=name)
    return render(req, 'teams/show.html', {"team": team})


def do_login(request):
    if request.method == "POST":
        form = TokenAuthForm(data=request.POST)
        if form.is_valid():
            team = authenticate(token=form.cleaned_data['token'])

            # Don't know why, but don't allow to login staff and admins via main form
            if team is not None and not team.is_staff and not team.is_superuser:
                login(request, team)
                return redirect("home")
            else:
                if team is None:
                    form.errors['token'] = form.error_class(["Wrong token"])
                else:
                    form.errors['token'] = form.error_class(["Special users can't login by token"])
        return render(request, "teams/login.html", {"form": form})
    else:
        return render(request, "teams/login.html", {"form": TokenAuthForm()})


def do_logout(request):
    logout(request)
    return redirect("home")