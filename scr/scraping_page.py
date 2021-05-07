import requests
from unidecode import unidecode
from bs4 import BeautifulSoup
from scr.logs import *


# Função que pega as avaliações da imprensa e do AdoroCinema.
# Ela recebe como entrada apenas um filme da lista dos resultados e suas informações. Assim, ela retira as informações
# Nome e Nota de cada avaliação.
def film_rate(single_re):
    # print(single_re)
    # Cada info é uma possível nota. Podem ocorrer notas vazias e ausência de avaliações.
    # Filtra o resultado pelas classes rating-item-content
    info = single_re.find_all(class_="rating-item-content")
    # Variável que guarda uma lista de lista com o Nome e a Nota da avaliação, Ex: [[AdoroCinema, 4], [Crítica, 3]]
    list_of_notes = []
    # Para cada avaliação dentro do filme
    for f in info:
        # Cria uma lista que armazena o Nome e Nota de uma única avaliação
        tuple_rate = []
        # Separa as informações úteis da avaliação. i é uma tupla do tipo [<>,<>]
        i = f.find_all('span')
        # print(i)
        # Para cada valor presente em i, devemor retirar apenas o conteúdo. Dessa forma, obtém-se o [Nome, Nota]
        for a in i:
            tuple_rate.append(a.contents[0])
        # Adiciona a tupla na lista de lista que contém as avaliações, se não for vazio ou faltar dados
        if len(tuple_rate) == 2:
            list_of_notes.append(tuple_rate)
    # Retorna a lista com as avaliações
    return list_of_notes


# Função que pega o nome do filme de logs e monta o link de pesquisa no site
def build_link():
    # Removendo acentos e colocando as letras em minúsculo
    film = film_name.replace(" ", "+")
    film = unidecode(film)
    film = film.lower()
    # Montando o link de pesquisa
    page = "https://www.adorocinema.com/pesquisar/movie/?q=" + film
    return page


# Função que faz o request. Após isto, os dados serão tratados com o BeatifulSoup
def make_request():
    # Chama função que constrói link de pesquisa
    page = build_link()
    # Fazendo Request
    req = requests.get(page, proxies, timeout=120)
    # Pegando contúdo
    r = req.content
    # Chama a função que faz o tratamento dos dados obtidos na página html
    return data_parser(r)


# Função que faz o tratamento dos dados obtidos em html, para extrair a informação útil
def data_parser(r):
    # Pegando dados do arquivo HTML com o BeatifulSoup
    data = BeautifulSoup(r, 'html.parser', from_encoding='utf_8')
    # Pega todos os resultados da pesquisa e todas as informações sobre cada um deles
    result = data.find_all("li")
    # Os filmes estão organizados em colunas na classe = "section movies-results", divididos pelo "h2"
    # Lista que armazena os nomes de cada um dos títulos dos resultados
    list_of_names = []
    # Percorre a lista dos resultados, separando apenas o nome do filme e ignorando as demais informações
    notes = []
    for re in result:
        # Se o resultado não for vazio, significa que existe algum filme que corresponde à pesquisa
        if re.find_all("h2"):
            # Adiciona o nome do filme à lista com os nomes mostrados após a pesquisa
            # A função contents retira apenas o conteúdo contido no trecho HTML [Sessão H2]
            list_of_names.append(re.find_all("h2")[0].contents[1].contents[0])
            # Para cada filme retornado, busca todas as avaliações presentes e adiciona na lista notes
            notes.append(film_rate(re))

    return list_of_names, notes
