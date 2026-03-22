from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Jogador, Partida
from . import services
from django.db.models import Count

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

@login_required
def jogar(request):
    perguntas = services.gerar_perguntas(quantidade=10)
    request.session['perguntas'] = perguntas
    request.session['indice'] = 0
    request.session['acertos'] = 0
    return redirect('pergunta')

@login_required
def pergunta(request):
    perguntas = request.session.get('perguntas')
    indice = request.session.get('indice', 0)

    if not perguntas or indice >= len(perguntas):
        return redirect('resultado')

    return render(request, 'quiz/pergunta.html', {
        'pergunta': perguntas[indice],
        'numero': indice + 1,
        'total': len(perguntas),
    })

@login_required
def responder(request):
    if request.method != 'POST':
        return redirect('pergunta')

    perguntas = request.session.get('perguntas', [])
    indice = request.session.get('indice', 0)
    acertos = request.session.get('acertos', 0)

    resposta = request.POST.get('resposta')
    capital_correta = perguntas[indice]['capital_correta']

    if resposta == capital_correta:
        acertos += 1
        request.session['acertos'] = acertos

    request.session['indice'] = indice + 1
    return redirect('pergunta')

@login_required
def resultado(request):
    acertos = request.session.get('acertos', 0)
    total = len(request.session.get('perguntas', []))
    pontuacao = acertos * 10

    jogador, _ = Jogador.objects.get_or_create(usuario=request.user)
    Partida.objects.create(
        jogador=jogador,
        modo='capitais',
        total_perguntas=total,
        acertos=acertos,
        pontuacao=pontuacao,
    )
    jogador.pontuacao_total += pontuacao
    jogador.save()

    request.session.flush()

    return render(request, 'quiz/resultado.html', {
        'acertos': acertos,
        'total': total,
        'pontuacao': pontuacao,
    })

def ranking(request):
    jogadores = Jogador.objects.select_related('usuario').annotate(num_partidas=Count('partidas')).order_by('-pontuacao_total')[:10]
    return render(request, 'quiz/ranking.html', {'jogadores': jogadores})

@login_required
def perfil(request):
    jogador, _ = Jogador.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        nova_bio = request.POST.get('bio', '').strip()
        jogador.bio = nova_bio
        jogador.save()
        return redirect('perfil')
        
    partidas = Partida.objects.filter(jogador=jogador).order_by('-data')
    return render(request, 'quiz/perfil.html', {
        'jogador': jogador,
        'partidas': partidas
    })

@login_required
def deletar_conta(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('home')
    return redirect('perfil')

