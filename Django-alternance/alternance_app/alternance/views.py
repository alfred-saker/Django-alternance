
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect ,get_object_or_404
from alternance.forms import UserRegistrationForm,UserLoginForm,OffreForm
from alternance.models import Offre, User


def home_view(request):
  user_id = request.user.id
  username = request.user.username
  datas = Offre.objects.filter(user_id=user_id)
  return render(request, 'home.html',{'datas':datas, 'user_id':user_id,'username':username})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'Auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Identifiants invalides.')
    
    form = UserLoginForm()
    return render(request, 'Auth/login.html', {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')

# @login_required
def add_view(request):
    if request.method == "POST":
        form = OffreForm(request.POST)
        if form.is_valid():
            offre = form.save(commit=False)
            user = get_object_or_404(User, id_user=request.user.id)  # Récupérer l'objet User correspondant à l'ID de l'utilisateur connecté
            offre.user = user
            offre.save()
            return redirect('home')
        else:
            print(form.errors) 
    else:
        form = OffreForm(initial={'user': request.user.id})  # Pré-remplissage du champ user dans le formulaire initial
    return render(request, "add_offre.html", {"form": form})