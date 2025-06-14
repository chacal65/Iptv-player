import requests
import json

def link_ativo(url):
    try:
        r = requests.get(url, timeout=5)
        return r.status_code == 200
    except:
        return False

def verificar_canais():
    with open('canais.json', 'r') as file:
        canais = json.load(file)

    canais_verificados = {}

    for nome, links in canais.items():
        ativos = [link for link in links if link_ativo(link)]
        if ativos:
            canais_verificados[nome] = ativos

    with open('canais.json', 'w') as file:
        json.dump(canais_verificados, file, indent=4)

if __name__ == "__main__":
    verificar_canais()
