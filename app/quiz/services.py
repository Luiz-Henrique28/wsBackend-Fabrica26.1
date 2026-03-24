import random
import requests

API_URL = "https://restcountries.com/v3.1/all?fields=name,capital,population,flags,translations"

_cache_paises = None

def buscar_paises():
    global _cache_paises
    if _cache_paises is None:
        resposta = requests.get(API_URL, timeout=10)
        resposta.raise_for_status()
        _cache_paises = []
        for p in resposta.json():
            if p.get('capital') and p.get('name', {}).get('common'):
                nome_pt = p.get('translations', {}).get('por', {}).get('common')
                if nome_pt:
                    p['name']['common'] = nome_pt
                _cache_paises.append(p)
    return _cache_paises

def gerar_perguntas(quantidade=10):
    paises = buscar_paises()
    selecionados = random.sample(paises, quantidade)
    outros = [p for p in paises if p not in selecionados]
    perguntas = []

    for pais in selecionados:
        opcoes_erradas = random.sample(outros, 3)
        tipo = random.choice(['capital', 'bandeira', 'populacao'])

        if tipo == 'capital':
            texto = f"Qual é a capital de {pais['name']['common']}?"
            correta = pais['capital'][0]
            opcoes = [correta] + [p['capital'][0] for p in opcoes_erradas]
            imagem = ""
        
        elif tipo == 'bandeira':
            texto = "A qual país pertence esta bandeira?"
            correta = pais['name']['common']
            opcoes = [correta] + [p['name']['common'] for p in opcoes_erradas]
            imagem = pais['flags'].get('png', '')
            
        elif tipo == 'populacao':
            grupo = [pais] + opcoes_erradas
            pais_maior = max(grupo, key=lambda x: x.get('population', 0))
            
            texto = "Qual destes países possui a MAIOR população?"
            correta = pais_maior['name']['common']
            opcoes = [p['name']['common'] for p in grupo]
            imagem = ""

        random.shuffle(opcoes)
        pergunta = {
            'texto': texto,
            'bandeira': imagem,
            'capital_correta': correta,
            'opcoes': opcoes
        }
        perguntas.append(pergunta)

    return perguntas
