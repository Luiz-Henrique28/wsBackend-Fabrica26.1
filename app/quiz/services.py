import random
import requests

API_URL = "https://restcountries.com/v3.1/all?fields=name,capital,population,flags"

_cache_paises = None

def buscar_paises():
    global _cache_paises
    if _cache_paises is None:
        resposta = requests.get(API_URL, timeout=10)
        resposta.raise_for_status()
        _cache_paises = [
            p for p in resposta.json()
            if p.get('capital') and p.get('name', {}).get('common')
        ]
    return _cache_paises

def gerar_perguntas(quantidade=10):
    paises = buscar_paises()
    selecionados = random.sample(paises, quantidade)
    perguntas = []

    for pais in selecionados:
        outros = [p for p in paises if p != pais]
        opcoes_erradas = random.sample(outros, 3)

        pergunta = {
            'pais': pais['name']['common'],
            'bandeira': pais['flags'].get('png', ''),
            'capital_correta': pais['capital'][0],
            'opcoes': sorted(
                [pais['capital'][0]] + [p['capital'][0] for p in opcoes_erradas],
                key=lambda x: random.random()
            )
        }
        perguntas.append(pergunta)

    return perguntas
