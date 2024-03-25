from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                login(request, user)
                return HttpResponse("You are now logged in!")
            else:
                return HttpResponse("Incorrect username and/or password.")
        else:
            return HttpResponse("Invalid login.")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {"form": form})
