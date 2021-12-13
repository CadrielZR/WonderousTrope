#biblioteca(s) utilizada(s)
from crawler import scraper

#termo de pesquisa recebe input de usuário
search = input()

#transforma string em lista (strings no python são imutáveis)
search = list(search)

#transforma espaços em '+' já que é o modo como as urls funcionam
for i in range(len(search)):
    if search[i] == ' ':
        search[i] = '+'

#transforma lista em string novamente
search = ''.join(search)

#chama método de scraping tendo o termo de busca como parâmetro
link = scraper(search)

print('\n{}'.format(link))