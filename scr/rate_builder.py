from unidecode import unidecode
from scr.logs import *


# Função que recebe a lista com todos os filmes resultantes da busca e verifica algum item foi retornado
def verify(list_of_names):
    # Encerra a execução do programa caso nenhum filme seja encontrado com a pesquisa
    if not list_of_names:
        print("Nenhum filme encontrado com este nome: ", film_name)
        exit(0)


# Função que busca o filme na lista de resultados e exibe sua avaliação, caso possua
def rating(list_of_names, notes):
    """ Esta função pode necessitar de ajustes posteriores para identificar filmes diferentes com nomes iguais,
    com base no ano, atores,popularidade ou mesmo uma escolha do usuário """

    # Percorre a lista de nomes e encontra o PRIMEIRO filme correspondente ao requerido
    for position in range(0, len(list_of_names)):
        if unidecode(list_of_names[position]).lower() == unidecode(film_name).lower():
            print('-----------------------------------------------')
            print("Filme buscado: ", film_name)
            print('-----------------------------------------------')
            print("Avaliações: ")
            print('-----------------------------------------------')
            # Printa as notas de cada crítica, removendo espaços remanescentes
            if notes[position]:
                for rate in notes[position]:
                    n = rate[0].strip()
                    r = rate[1].strip()
                    if r is not None and n is not None:  # Se possuir nota
                        print(n, ": ", r)
            else:
                print("Não possui avaliações")
            print("-----------------------------------------------")
            break
