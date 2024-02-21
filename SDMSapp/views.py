from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import PlayerForm, Player, DepartmentForm, Sportform


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # Handle invalid login
            return render(request, 'SDMSapp/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'SDMSapp/login.html')

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'SDMSapp/signup.html', {'form': form})

@login_required
def user_home(request):
    return render(request, 'SDMSapp/home.html')

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SDMSapp/player_list')  # Redirect to player list page after successful form submission
    else:
        form = PlayerForm()
    return render(request, 'SDMSapp/addplayer.html', {'form': form})

def player_list(request):
    players = Player.objects.all()
    return render(request, 'SDMSapp/player_list.html', {'players': players})



