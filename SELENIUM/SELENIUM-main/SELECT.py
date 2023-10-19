from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.imdb.com/title/tt0120338/videogallery/")

from selenium.webdriver.support.ui import Select

elementSelect = Select( navegador.find_element(By.NAME, "sort" ))

elementSelect.select_by_value('value')

navegador.implicity_wait(2)

elementSelect = Select(navegador.find_element(By.NAME, "sort"))
elementSelect.select_by_visible_text("Date")

elementSelect = Select(navegador.find_element(By.NAME, "sort"))
Select(navegador.find_element(By.NAME, "sort")).select_by_index(1)