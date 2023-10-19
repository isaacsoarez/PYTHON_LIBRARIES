from selenium import webdriver
#Importar o web driver da biblioteca selenium

#Denro do webdriver, temos o webdriver_manager, que é utilizado para informar o navegador que esta sendo utilizado

from webdriver_manager.chrome import ChromeDriveManager

#Como usaremos diversos recursos dentro do navegador, teremos que habilitaralguns serviços, portanto, vamos habilitar a function SERVICES  do WEBDRIVER.

fromselenium.webdriver.chrome.service import Service

#Ao importarmos a função SERVICE, deveremos por boas práticas colocar todas as suas carscteristicas em uma variavel

servico = Service(ChromeDriverManager().install())

#Sempre  criamos uma variavel para usar o webdriver e o service 

navegador = webdriver.Chrome(service=servico)
#Site = webdriver.Chrome(service=servico)
#Paginas = webdriver.Chrome(service=servico)

#vamos importar a biblioteca by, so selenium usamos para inspecionar e resgatar conteudos das tags(id, span, title, entre outras) das paginas HTML

from selenium.webdriver.common.by import by

#comando para abrir o navegador com uma pagina de site 

navegador.get('https://www.google.com.br')

#o comando abaixo, INSPECIONA o conteúdo de input no site do google e escreve uma pesquisa

navegador.find_element(By.XPATH, "[Aqui, pesquisaremos o XPATH no site acima que iremos citarpara permit6ir a escriyta da frase ]").sendkeys("digite o valor que quer pesquisar")