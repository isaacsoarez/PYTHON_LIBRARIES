from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#navegador.get("https://www.google.com.br")

servico = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

with webdriver.Chrome(Service=servico) as driver: 
    driver.get("https://pythonexamples.org")
    driver.find_element(By.LINK_TEXT, "OpenCV").click
    driver.refresh()
    #driver.back()