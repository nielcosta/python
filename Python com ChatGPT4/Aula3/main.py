import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configurando o WebDriver do Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executar o navegador em segundo plano, sem abrir uma janela
service = Service('caminho_para_o_executável_do_chrome_driver')  # Substitua pelo caminho para o executável do ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessar a URL
url = 'https://produto.mercadolivre.com.br/MLB-2068417303-bicicleta-aco-carbono-ksvj-aro-29-freios-a-disco-21-vel-_JM#position=40&search_layout=grid&type=item&tracking_id=b67cabfb-ad4f-4277-bf05-559c6812680f&c_id=/home/promotions-recommendations/element&c_element_order=2&c_uid=7a0d19a2-cee0-46ba-9f3a-fb5cc46f299d'
driver.get(url)

# Aguardar 5 segundos para a página carregar completamente
time.sleep(5)

# Localizar o elemento <h1 class="ui-pdp-title"> e imprimir o nome do produto
titulo_element = driver.find_element(By.CLASS_NAME, 'ui-pdp-title')
nome_produto = titulo_element.text
print(f'Nome do produto: {nome_produto}')

# Localizar o elemento <span class="andes-money-amount__fraction"> e obter o valor do produto como float
valor_element = driver.find_element(By.CLASS_NAME, 'andes-money-amount__fraction')
valor_texto = valor_element.text.replace('.', '').replace(',', '.')
valor = float(valor_texto)
print(f'Valor do produto: R${valor:.2f}')

# Verificar se o valor é menor que R$1000.00 e imprimir "Bom para Compra" se for o caso
if valor < 1000.00:
    print('Bom para Compra')

# Fechar o navegador
driver.quit()