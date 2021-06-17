from browser import Browser,Keys
import time

# [Classe que herda as condições do script Browser.py, aqui é onde criamos as funções de pesquisa para uma
# página em específico no site do Mantis, no caso desta classe, ela é específica para a
# página PRINCIPAL, também chamada de DASHBOARD, onde temos o controle das principais abas]
class DashboardPage(Browser):

    #Esta função procura e retorna o titulo da página principal
    def get_titulo(self):
        return self.driver.find_element_by_class_name("menu-text").text

    # Esta função mostra o usuário logado através de um pop-up na página
    def show_usuario(self,usuario):
        self.driver.execute_script("alert('Login Bem Sucedido como: "+usuario+"')")
        time.sleep(2)
        self.driver.switch_to.alert.accept()

    # Esta função procura e nome do usuário na página principal
    def get_nome(self):
        return self.driver.find_element_by_xpath('//*[@id="breadcrumbs"]/ul/li/a').text

    # Esta função procura e cargo na página principal
    def get_cargo(self):
        return self.driver.find_element_by_xpath('//*[@id="breadcrumbs"]/ul/li/span').text

    # Esta função acessa o primeiro item da aba lateral esquerda que no caso é o próprio DASHBOARD
    def main(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[1]/a/span').click()

    # Esta função acessa o segundo item da aba lateral esquerda que no caso é o "Ver Tarefas"
    def ver_tarefas(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a/span').click()

    # Esta função acessa o terceiro item da aba lateral esquerda que no caso é o "Criar Tarefa"
    def criar_tarefa(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[3]/a/span').click()

    # Esta função acessa o quarto item da aba lateral esquerda que no caso é o "Registro de Mudanças"
    def registro_mudanca(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[4]/a/span').click()

    # Esta função acessa o quinto item da aba lateral esquerda que no caso é o "Planejamentos"
    def planejamentos(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[5]/a/span').click()

    # [Esta função acessa o menu de dropdown do canto superior direito na dashboard, assim mostrando algumas
    # opções extras.]
    def user_info(self):
        self.driver.find_element_by_class_name('user-info').click()

    # [Esta função é um complemento do user_info(), onde aqui acessamos um item dentro do menu dropdown
    # chamado "Minha Conta"]
    def minhaConta(self):
        self.driver.find_element_by_xpath('//*[@id="navbar-container"]/div[2]/ul/li[2]/ul/li[1]/a').click()

    # [Esta função é um complemento do user_info(), onde aqui acessamos um item dentro do menu dropdown
    # chamado "Sair"]
    def sair(self):
        self.driver.find_element_by_xpath('//*[@id="navbar-container"]/div[2]/ul/li[2]/ul/li[4]/a').click()
        self.driver.execute_script("alert('LOGOUT BEM SUCEDIDO')")
        time.sleep(1)
        self.driver.switch_to.alert.accept()

