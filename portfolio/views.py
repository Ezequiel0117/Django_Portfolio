from django.shortcuts import redirect, render
from .models import Project, Experiences
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    projects = Project.objects.all()
    experiences = Experiences.objects.all()
    
    return render(request, 'home.html', {'projects': projects, 'experiences': experiences})

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {
            "form": UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST
                    ['password1'])
                user.save()
                login(request, user)  # Crear cookie y redireccionarlo
                # Return para una vez que termine ahi una vez que se guarde el usuario
                return redirect('home')
            except IntegrityError:
                return render(request, "signup.html", {
                    'form': UserCreationForm,
                    "error": 'Username already exists'
                })
        return render(request, "signup.html", {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })
        
def signout(request):
    logout(request)
    # Return para redireccionar al home después de cerrar sesión
    return redirect('home')


def siging(request):
    if request.method == 'GET':
        return render(request, "signin.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'],password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')
