from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import User, Post, Like, Follow


def index(request):
    return render(request, "network/index.html", {
        "postings": Post.objects.all(),
        "create": newPost()
    })

def following(request):
    return render(request, "network/index.html", {
        "postings": Post.objects.filter(writer=User.objects.get(username=request.user)),
    })

def profile(request, profileName):
    followedCount = 0
    followingCount = 0
    for post in Follow.objects.filter(follower=User.objects.get(username=profileName)):
        followingCount += 1
    for post in Follow.objects.filter(followed=User.objects.get(username=profileName)):
        followingCount += 1
    return render(request, "network/profile.html", {
        "userProfile": User.objects.get(username=profileName),
        "userPosts": Post.objects.filter(writer=User.objects.get(username=profileName)),
        "following": followingCount,
        "followed": followedCount,
        "follow": followUser()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

class newPost(forms.Form):
    content = forms.CharField(widget=forms.Textarea(), label="New Post")
class followUser(forms.Form):
    content = forms.BooleanField(label="Follow User")
