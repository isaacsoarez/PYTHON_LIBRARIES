from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
from selenium.webdriver.common.by import By

#ispencionando um site de investimentos (STATUSINVEST)

navegador.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

navegador.implicitly_wait(3)

#inspecionando conteudo por classe
dados1 = navegador.find_elements(By.TAG_NAME, "h3")[1].text
dados2 = navegador.find_elements(By.TAG_NAME, "strong")[0].text
dados3 = navegador.find_elements(By.TAG_NAME, "span")[1].text
dados4 = navegador.find_elements(By.TAG_NAME, "div")[2].text

print(dados1)
print(dados2)
print(dados3)
print(dados4)


