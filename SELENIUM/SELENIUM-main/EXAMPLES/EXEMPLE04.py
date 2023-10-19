from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
from selenium.webdriver.common.by import By

navegador.get("https://statusinvest.com.br/fundos-imobiliarios/knrill")

navegador.implicity_wait(3)

nomeFii = navegador.find_elements(By.ID, "h1")[0].text
valorAtual = navegador.find_elements(By.ID, "strong1")[0].text
tableRendimentos = navegador.find_elements(By.ID, "table")[0].text
tableResultados = navegador.find_elements(By.ID, "table")[1].text

print(nomeFii)
print(valorAtual)
print(tableRendimentos)
print(tableResultados)