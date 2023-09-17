from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pdb


print ('Iniciando o Robo...')
driver = webdriver.Chrome()
driver.get("https://registro.br")
time.sleep(5)


dominios =["robopython.com", "oglobo.com", "danielmendes.info", "pythonextra.com.br"]


for dominio in dominios:
    pesquisa = driver.find_element(By.ID, 'is-avail-field')
    time.sleep(2)
    pesquisa.send_keys(Keys.CLEAR)
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.ENTER)
    time.sleep(3)
    resultados = driver.find_elements(By.TAG_NAME, 'strong')
    print('Dominio : %s - %s '% (dominio ,resultados[2].text))