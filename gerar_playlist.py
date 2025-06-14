import json

def gerar_m3u():
    with open('canais.json', 'r') as file:
        canais = json.load(file)

    m3u = "#EXTM3U\n"

    for nome, links in canais.items():
        if links:
            m3u += f'#EXTINF:-1,{nome}\n{links[0]}\n'

    with open('lista.m3u', 'w') as file:
        file.write(m3u)

if __name__ == "__main__":
    gerar_m3u()
