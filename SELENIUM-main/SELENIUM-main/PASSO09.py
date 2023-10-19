from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("file:///C:/Users/Aluno/Desktop/ISAAC/PASSO09.html")

from selenium.webdriver.support.ui import Select


elementSelect = Select( navegador.find_element(By.NAME, "selectomatic" ))
elementSelect.select_by_value('one')

elementSelect = Select( navegador.find_element(By.NAME, "selectomatic" ))
elementSelect.select_by_value('two')

elementSelect = Select( navegador.find_element(By.NAME, "selectomatic" ))
elementSelect.select_by_value('four')

elementSelect = Select( navegador.find_element(By.NAME, "selectomatic" ))
elementSelect.select_by_value('still learning how to count, apparently')

valor_select = elementSelect.select_by_value('one')
#elementSelect = Select(navegador.find_element(By.NAME, "selectomatic"))
#Select(navegador.find_element(By.NAME, "still learning how to count, apparently")).select_by_index(1)
print (valor_select)
print (elementSelect.select_by_value('one'))
print (elementSelect.select_by_value('two'))
print (elementSelect.select_by_value('four'))
print (elementSelect.select_by_value('still learning how to count, apparently'))