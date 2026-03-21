from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Jogador

def home(request):
    return render(request, 'quiz/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Jogador.objects.create(usuario=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'quiz/register.html', {'form': form})
