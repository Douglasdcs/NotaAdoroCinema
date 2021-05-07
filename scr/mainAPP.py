import requests
from unidecode import unidecode
from bs4 import BeautifulSoup


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

# Quarta Etapa

'''Esta função pode necessitar de ajustes posteriores para identificar filmes diferentes com nomes iguais, 
com base no ano, atores,popularidade ou mesmo uma escolha do usuário '''

# Determinando qual filme é o requerido pelo usuário
# Percorre a lista de nomes e encontra o primeiro filme correspondente
for position in range(0, len(list_of_names)):
    if unidecode(list_of_names[position]).lower() == unidecode(film_name).lower():
        break


# Solução: buscar todos os "rating-item-content", dentro deles separar notas entre imprensa e AdoroCinema,
# usando o resultado presente em result. Isso garantirá que possa ser armazenado uma tupla [[filme1, nota A, nota B ..]]
# Assim, ao enontrarmos o nome do filme, printaremos todas as notas

lista = []

i = 1
for re in result:
    aux = []
    if re.find_all(class_='rating-item-content'):
        aux.append(re.find_all(class_='rating-item-content')[0])
        a = re.find_all(class_='rating-item-content')[0]
        print(i, '\n----\n', re.find_all(class_='rating-item-content')[0])
        a = a.find_all('span')
        # print(i, '\n----\n', a)
        lista.append(a)
        i = i+1

print(lista)
# print(aux)


