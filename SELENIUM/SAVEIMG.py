from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import urllib.request

servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico)

nav.get("https://www.cnnbrasil.com.br")
nav.implicitly_wait(2)

# Encontra o elemento da imagem
classimg = nav.find_element(By.CLASS_NAME, "three__highlights__img")
srcatribute = classimg.get_attribute("src")
print(srcatribute)

try:
    # Salvar a imagem
    urllib.request.urlretrieve(srcatribute, r"C:\Users\Aluno\Desktop\ISAAC\img\minha_imagem.jpg")
    print("IMAGEM SALVA")
except Exception as e:
    print(f"ERROR as save")

nav.quit(3)
