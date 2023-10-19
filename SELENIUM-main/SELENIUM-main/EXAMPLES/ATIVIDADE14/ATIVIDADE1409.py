from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://pythonexamples.org/tmp/selenium/index-56.html")

navegador.implicitly_wait(3)

dados1 = navegador.find_elements(By.TAG_NAME, "div")[0].text
dados2 = navegador.find_element(By.TAG_NAME, "p")
dados3 = navegador.find_elements(By.TAG_NAME, "div")[1].text
dados4 = navegador.find_element(By.TAG_NAME, "a").text

print("--------////-----------////-----")
print(dados1)
print("--------////-----------////-----")
print(dados2)
print("--------////-----------////-----")
print(dados3)
print("--------////-----------////-----")
print(dados4)
print("--------////-----------////-----")
