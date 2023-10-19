from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
#SUBIR E DESCER BARRA DO SITE
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.cnnbrasil.com.br/economia/")
navegador.implicitly_wait(2)

navegador.execute_script("window.scrollTo(0, window.innerHeight);")
time.sleep(3)
time.sleep(3)

navegador.execute_script("window.scrollTo(0, 0);")
time.sleep(3)
time.sleep(3)

navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
time.sleep(3)


navegador.quit