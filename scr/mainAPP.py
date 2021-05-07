import requests
from unidecode import unidecode
from bs4 import BeautifulSoup


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
        tuple = []
        # Separa as informações úteis da avaliação. i é uma tupla do tipo [<>,<>]
        i = f.find_all('span')
        # print(i)
        # Para cada valor presente em i, devemor retirar apenas o conteúdo. Dessa forma, obtém-se o [Nome, Nota]
        for a in i:
            tuple.append(a.contents[0])
        # Adiciona a tupla na lista de lista que contém as avaliações, se não for vazio ou faltar dados
        if len(tuple) == 2:
            list_of_notes.append(tuple)
    # Retorna a lista com as avaliações
    return list_of_notes

# Primeira Etapa

# Realizando a entrada do nome do filme
film_name = "Missão Impossível"
# Removendo acentos e colocando as letras em minúsculo
film = film_name.replace(" ", "+")
film = unidecode(film)
film = film.lower()
# Montando o link de pesquisa
page = "https://www.adorocinema.com/pesquisar/movie/?q=" + film
# print(page)

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
notes = []
for re in result:
    # Se o resultado não for vazio, significa que existe algum filme que corresponde à pesquisa
    if re.find_all("h2"):
        # Adiciona o nome do filme à lista com os nomes mostrados após a pesquisa
        # A função contents retira apenas o conteúdo contido no trecho HTML
        list_of_names.append(re.find_all("h2")[0].contents[1].contents[0])
        # Para cada filme retornado, busca todas as avaliações presentes e adiciona na lista notes
        notes.append(film_rate(re))

# Encerra a execução do programa caso nenhum filme seja encontrado com a pesquisa
if not list_of_names:
    print("Nenhum filme encontrado com este nome: ", film_name)
    exit(0)

# Quarta Etapa

'''Esta função pode necessitar de ajustes posteriores para identificar filmes diferentes com nomes iguais, 
com base no ano, atores,popularidade ou mesmo uma escolha do usuário '''

# Determinando qual filme é o requerido pelo usuário
# Percorre a lista de nomes e encontra o primeiro filme correspondente
for position in range(0, len(list_of_names)):
    if unidecode(list_of_names[position]).lower() == unidecode(film_name).lower():
        print('-------------------')
        print("Filme buscado: ", film_name)
        print("-------------------\nAvaliações: \n-------------------")
        # Printa as notas de cada crítica, removendo espaços remanescentes
        for rate in notes[position]:
            n = rate[0].strip()
            r = rate[1].strip()
            print(n, ": ", r)
        print("-------------------")
        break


# print(list_of_names)
# print(len(list_of_names))
# print(notes)
# print(len(notes))

if __name__ == "__main__":
    print("Ola")

