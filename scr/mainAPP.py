import requests
from unidecode import unidecode
from bs4 import BeautifulSoup


# Primeira Etapa

# Realizando a entrada do nome do filme
film = "Missão Impossível"
# Removendo acentos e colocando as letras em minúsculo
film = film.replace(" ", "+")
film = unidecode(film)
film = film.lower()
# Montando o link de pesquisa
page = "https://www.adorocinema.com/pesquisar/movie/?q=" + film

# Segunda Etapa

# Definindo Proxies
proxies = {'https': '192.167.20.3:8080', 'http': '192.167.20.3:8080'}
# Fazendo Request
req = requests.get(page, proxies, timeout=120)
# Pegando contúdo
r = req.content

# Terceira Etapa

# Pegando dados do arquivo HTML com o BeatifulSoup
data = BeautifulSoup(r, 'html.parser', from_encoding='utf_8')
# Buscando resultados da pesquisa
result = data.find_all("h2")
# Os filmes estão organizados em colunas na classe = "section movies-results", divididos pelo "h2"

# Se o resultado for vazio, imprime uma mensagem e finaliza a execução
if not result:
    print("Filme não encontrado")
    exit(0)
else:
    results = []
    # Percorre a lista dos filmes e retira o conteúdo que importa
    for re in result:
        results.append(re.contents[1].contents[0])
    print(results)

