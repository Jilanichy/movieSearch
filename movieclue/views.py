from .forms import *
from movieclue.services import *
import requests
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    form = SearchMovieForm()
    context = {
        "form": form
    }
    return render(request, 'search.html', context)


def find(request):
    if request.method == 'GET':
        form = SearchMovieForm(request.GET)

        if form.is_valid():
            search_key = form.cleaned_data.get('search', '')
            year = form.cleaned_data.get('year', '')

        # For a single movie/series search
        if '+' not in search_key:
            movie_details = find_a_movie(form)
            return render(request, 'result.html', movie_details)

        # For multiple movie/series search using '+' as a delimiter
        else:
            desired_movies = find_many_movies(form)
            return render(request, 'results.html', {'movies': desired_movies})


def movie_list(request):
    response = requests.get("http://www.omdbapi.com/?s=batman&apikey=d7732e8d")
    data = response.json()

    movie_info = data['Search']
    for movie in movie_info:
        title = movie['Title']
    return render(request, 'results.html', {'movies': movie_info, 'title': title})
