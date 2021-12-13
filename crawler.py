#biblioteca(s) utilizada(s)
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''obs: o Edge me pareceu, durante os testes, o mais eficiente no carregamento de imagens'''

#acessa opções do webdriver a ser utilizado
op = webdriver.EdgeOptions()
#adiciona 'headless' (esconde o navegador)
op.add_argument('headless')

#definindo driver como Microsoft Edge (apague 'options = op' para ver o navegador em tempo real)
driver = webdriver.Edge(options = op)

#cria lista de imagens
images = []

#método de web scraping
'''(obs: é normal que o crawler demore aproximadamente 1 min para concluir)'''
def scraper(query):
    #coloca url abaixo para pular para o Google Imagens (query é o termo de pesquisa passado na main.py)
    driver.get('https://www.google.com/search?q={}&tbm=isch'.format(query))

    #faz o navegador procurar todos elementos com classe 'islib', ou seja, todas as imagens do resultado da pesquisa
    elem = driver.find_elements(By.XPATH, '//a[contains(@class,"islib")]')

    #para cada imagem encontrada pelo comando anterior
    for temp in elem:
        #escolhe a imagem através do href
        temp.get_attribute('href')

        #navegador clica na miniatura da imagem fazendo seus dados carregarem
        temp.click()

        #tempo de espera para que os dados carreguem (pode não ser o suficiente se a imagem for de alta resolução)
        time.sleep(1)

        #encontra local onde a fonte real da imagem está através do xpath inserido
        temp = driver.find_element(By.XPATH, '//div[@data-lhcontainer]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img')

        #cria tupla com apenas um elemento utilizando atributo source dentro do xpath anterior
        tupla1 = (temp.get_attribute('src'),)
        #print(temp.get_attribute('src'))

        #encontra local onde url da fonte está através do xpath inserido
        temp = driver.find_element(By.XPATH, '//div[@data-lhcontainer]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[3]/div[1]/a')

        #adiciona tupla anterior com uma recém criada que possui href através do xpath inserido formando uma de dois elementos
        tupla = tupla1 + (temp.get_attribute('href'),)
        #print('--',temp.get_attribute('href'))

        #insere tupla recém formada dentro da lista
        images.append(tupla)

    #escolhe tupla aleatória dentro da lista ao final do loop e retorna-a
    return(random.choice(images))