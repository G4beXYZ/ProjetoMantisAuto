from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Aqui é onde fica a classe principal para a execução do Webdriver
#APENAS MODIFIQUE SE SOUBER O QUE ESTÁ FAZENDO
#CASO O CONTRÁRIO RECOMENDO CRIAR UM CAMINHO PARA O WEBRDIVER IGUAL ESTA NO "PATH" ABAIXO
class Browser:
    #caminho padrão para o webdriver
    PATH = "C:\webdriver\chromedriver.exe"

    #[Declarando uma variavel com o valor do webdriver para carregar os seus valores com maior facilidade
    #nos outros scripts]
    driver = webdriver.Chrome(PATH)
    #Ajuste de janela do webdriver.(Caso queira mudar, troque apenas os valores do width e do height)
    driver.set_window_size(width=1920,height=740,windowHandle='current')
