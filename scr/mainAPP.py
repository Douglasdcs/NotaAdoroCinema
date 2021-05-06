import requests
from unidecode import unidecode
from bs4 import BeautifulSoup


# Primeira Etapa

# Realizando a entrada do nome do filme
film_name = "Missão Impossíve"
# Removendo acentos e colocando as letras em minúsculo
film = film_name.replace(" ", "+")
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
# Pega todos os resultados da pesquisa e todas as informações sobre cada um deles
result = data.find_all("li")
# Os filmes estão organizados em colunas na classe = "section movies-results", divididos pelo "h2"
# Lista que armazena os nomes de cada um dos títulos dos resultados
list_of_names = []
# Percorre a lista dos resultados, separando apenas o nome do filme e ignorando as demais informações
for re in result:
    # Se o resultado não for vazio, significa que existe algum filme que corresponde à pesquisa
    if re.find_all("h2"):
        # Adiciona o nome do filme à lista com os nomes mostrados após a pesquisa
        # A função contents retira apenas o conteúdo contido no trecho HTML
        list_of_names.append(re.find_all("h2")[0].contents[1].contents[0])

# Encerra a execução do programa caso nenhum filme seja encontrado com a pesquisa
if not list_of_names:
    print("Nenhum filme encontrado com este nome: ", film_name)
    exit(0)


