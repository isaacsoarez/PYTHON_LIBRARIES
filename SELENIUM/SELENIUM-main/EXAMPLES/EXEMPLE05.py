from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
from selenium.webdriver.common.by import By

#ispencionando um site de investimentos (STATUSINVEST)

navegador.get("https://www.imdb.com/")

navegador.implicitly_wait(2)

#inspecionando conteudo por classe
dados1 = navegador.find_elements(By.NAME, "q")[0]
dados2 = navegador.find_elements(By.NAME, "script")[1]
dados3 = navegador.find_elements(By.NAME, "main")[1]
dados4 = navegador.find_elements(By.NAME, "div")[1]

print(dados1)
print(dados2)
print(dados3)
print(dados4)


