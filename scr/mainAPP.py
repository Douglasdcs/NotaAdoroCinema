from scr.scraping_page import *
from scr.rate_builder import *


if __name__ == "__main__":
    # Chama a função que faz o scraping da página. Recebe a lista de nomes e avaliações dos filmes.
    list_of_names, notes = make_request()
    # Chama a função que verifica se algum filme foi encontrado
    verify(list_of_names)
    # Chama a função que verifica se o filme foi encontrado e se existe uma avaliação, exibindo-a caso positivo
    rating(list_of_names, notes)
