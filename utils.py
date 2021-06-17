from browser import Browser
from selenium.webdriver.common.keys import Keys
#[Aqui é onde fica a classe onde é armazenado algumas variáveis que serão utilizadas ao longo dos steps
#  criados.]
class UtilVars(object):
    USUARIO = 'INSIRA_USUARIO_AQUI'
    SENHA = 'INSIRA_SENHA_AQUI'
    USUARIO_COMPLETO = 'NOME_PAGINA_PRINCIPAL'
    CARGO = 'CARGO_AQUI'

#Aqui é a classe onde contém o acesso aos sites requisitados, no caso deste projeto, só foi utilizado 1 único link
class Utils(Browser):
    def entrar(self,url):
        self.driver.get(url)
