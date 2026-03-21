from django.db import models
from django.contrib.auth.models import User


class Jogador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='jogador')
    bio = models.TextField(blank=True, default='')
    pontuacao_total = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'
        ordering = ['-pontuacao_total']

    def __str__(self):
        return self.usuario.username


class Partida(models.Model):
    MODOS = [
        ('bandeiras', 'Bandeiras'),
        ('capitais', 'Capitais'),
        ('populacao', 'População'),
        ('misto', 'Misto'),
    ]

    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='partidas')
    modo = models.CharField(max_length=20, choices=MODOS, default='misto')
    total_perguntas = models.IntegerField(default=10)
    acertos = models.IntegerField(default=0)
    pontuacao = models.IntegerField(default=0)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'
        ordering = ['-data']

    def __str__(self):
        return f"Partida de {self.jogador.usuario.username} — {self.pontuacao} pts"
