from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
from selenium.webdriver.common.by import By

#Inspecionar o site INFOMONEY

navegador.get("https://www.infomoney.com.br/")

#gerar um atraso de 3 seg 

navegador.implicitly_wait(3)

#vamos pegar o conteudo de 1 das varias tags ID dado = navegador.find_element(By.ID, "high").text

#FIND_ELEMENTS, é utlizado quando obtiver mais  que uma tag como por exemplo a de ID 

dados1 = navegador.find_element(By.ID, "high").text
dados2 = navegador.find_elements(By.ID, "high")[0].text
dados3 = navegador.find_elements(By.ID, "high")[0].text
dados4 = navegador.find_elements(By.ID, "high")[2].text
dados5 = navegador.find_elements(By.ID, "high")[3].text


#Exibi o conteudo pesquisado
print("--------////-----------////-----")
print(dados1)
print("--------////-----------////-----")
print(dados2)
print("--------////-----------////-----")
print(dados3)
print("--------////-----------////-----")
print(dados4)
print("--------////-----------////-----")
print(dados5)


