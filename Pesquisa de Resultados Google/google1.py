from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

assunto = input("O que você deseja pesquisar no Google?: ")

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(2)
pesquisar = driver.find_element(By.NAME, "q")
time.sleep(2)
pesquisar.send_keys(assunto)
pesquisar.send_keys(Keys.ENTER)
time.sleep(8)
resultado = driver.find_element(By.ID, "result-stats").text
print(resultado)
numero_resultados = int(resultado.split("Aproximadamente ")[1].split(" resultados")[0].replace('.', ''))
numero_paginas = numero_resultados // 10
print(f"Número de Páginas: {numero_paginas}")

pagina_alvo = input(f"{numero_paginas} páginas encontradas, até qual página você quer ir?")
url_pagina = driver.find_element(By.LINK_TEXT, "2").get_attribute("href")

pagina_atual = 1
start = 10
lista_resultados = []

while pagina_atual <= int(pagina_alvo):
    if pagina_atual > 1:
        url_pagina = url_pagina.replace("start=%s" % start, "start=%s" % (start + 10))
        start += 10
        driver.get(url_pagina)
    pagina_atual += 1

    divs = driver.find_elements(By.CLASS_NAME, 'g')
    for div in divs:
        nome = div.find_element(By.TAG_NAME, "span")
        link = div.find_element(By.TAG_NAME, "a")
        resultado = f"{nome.text};{link.get_attribute('href')}"
        print(resultado)
        lista_resultados.append(resultado)

with open("resultados.txt", "w") as arquivo:
    for resultado in lista_resultados:
        arquivo.write(f"{resultado}\n")
    arquivo.close()

print(f"{len(lista_resultados)} resultados encontrados no Google e salvos no arquivo resultados.txt")
