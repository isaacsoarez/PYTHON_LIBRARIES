from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("C:/Users/Aluno/Desktop/ISAAC/PASSO09.html")

from selenium.webdriver.support.ui import Select
navegador.implicitly_wait(2)

elementSelect = Select( navegador.find_element(By.NAME, "selectomatic" ))
elementSelect.select_by_value('one')
time.sleep(5)


elementSelect = Select( navegador.find_element(By.NAME, "selectomatic" ))
elementSelect.select_by_value('two')
time.sleep(5)


elementSelect = Select( navegador.find_element(By.NAME, "selectomatic" ))
elementSelect.select_by_value('four')
time.sleep(5)


elementSelect = Select( navegador.find_element(By.NAME, "selectomatic" ))
elementSelect.select_by_value('still learning how to count, apparently')
time.sleep(5)


valor_select = elementSelect.select_by_value('one')
#elementSelect = Select(navegador.find_element(By.NAME, "selectomatic"))
#Select(navegador.find_element(By.NAME, "still learning how to count, apparently")).select_by_index(1)
print (elementSelect)
