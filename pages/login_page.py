from browser import Browser,Keys

# --------------------------------------------------------------------------------------------------------
# [Classe que herda as condições do script Browser.py, aqui é onde criamos as funções de pesquisa para uma
# página em específico no site do Mantis, no caso desta classe, ela é específica para a
# página de LOGIN]
class LoginPage(Browser):
    # Esta função serve para inserir automaticamente o usuário predefinido no campo de login
    def inserir_usuario(self,usuario):
        us = self.driver.find_element_by_id("username")
        us.send_keys(usuario)
        us.send_keys(Keys.RETURN)
    # Esta função serve para inserir automaticamente a senha predefinido no campo de login
    def inserir_senha(self,senha):
        psswd = self.driver.find_element_by_id("password")
        psswd.send_keys(senha)
        psswd.send_keys(Keys.RETURN)
