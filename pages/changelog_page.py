from browser import Browser,Keys

# --------------------------------------------------------------------------------------------------------
# [Classe que herda as condições do script Browser.py, aqui é onde criamos as funções de pesquisa para uma
# página em específico no site do Mantis, no caso desta classe, ela é específica para a
# página REGISTRO DE MUDANÇAS]

class ChangeLog(Browser):
    # [Esta função pega a escrita da pagina REGISTRO DE MUDANÇAS e retorna um texto que pode ser utilizado
    # para verificar se à algo no registro de mudanças ou não]
    def get_lead(self):
        return self.driver.find_element_by_class_name('lead').text
