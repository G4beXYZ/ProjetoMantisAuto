from browser import Browser,Keys
import time

# Classe especial para armazenar algumas variáveis com um valor fixo de uma pagina (facilita o acesso)
class TaskPageElements(object):
    STATE_ELEMENT = '//*[@id="main-container"]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div/table/tbody/tr[7]/td[1]'
    STATUS_ELEMENT = '//*[@id="main-container"]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div/table/tfoot/tr/td/div/div[3]/form/select/option[1]'
    SOLVED_ELEMENT = '//*[@id="main-container"]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div/table/tfoot/tr/td/div/div[3]/form/select/option[5]'
    APAGAR = '//*[@id="main-container"]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div/table/tfoot/tr/td/div/div[9]/form/fieldset/input[4]'
    CONFIRM_APAGAR = '//*[@id="action-group-div"]/form/div/div[2]/div[2]/input'
    BUTTON_ATUALIZAR = '//*[@id="main-container"]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div/table/tfoot/tr/td/div/div[3]/form/input[1]'
    BUTTON_CONFIRMAR_ATUALIZAR = '//*[@id="bug-change-status-form"]/fieldset/div/div[2]/div[2]/input'

# --------------------------------------------------------------------------------------------------------
# [Classe que herda as condições do script Browser.py, aqui é onde criamos as funções de pesquisa para uma
# página em específico no site do Mantis, no caso desta classe, ela é específica para a
# página de criação de uma tarefa]
class TaskPage(Browser):
    # Esta função retorna o estado da tarefa atual
    def get_state(self):
        return self.driver.find_element_by_xpath(TaskPageElements.STATE_ELEMENT).text

    # Esta função retorna o status da tarefa atual
    def get_status(self):
        return self.driver.find_element_by_xpath(TaskPageElements.STATUS_ELEMENT).get_attribute('selected')

    # Esta função modifica o status da tarefa atual para "resolvido"
    def mudar_status(self):
        self.driver.find_element_by_xpath(TaskPageElements.SOLVED_ELEMENT).click()

    # Esta função confirma as etapas de modificação para aplicar o novo status
    def atualizar_tarefa(self):
        self.driver.find_element_by_xpath(TaskPageElements.BUTTON_ATUALIZAR).click()
        self.driver.find_element_by_xpath(TaskPageElements.BUTTON_CONFIRMAR_ATUALIZAR).click()

    # [Esta função preenche os campos do formulário uma tarefa a ser criada
    # e depois automaticamente confirma a criação da tal tarefa]
    def preencher(self,testNumber):
        self.driver.find_element_by_xpath('//*[@id="reproducibility"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="severity"]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="priority"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="handler_id"]/option[3]').click()
        self.driver.find_element_by_id('summary').send_keys("Teste de resumo Automatico " + str(testNumber))
        self.driver.find_element_by_id('description').send_keys("Teste de descricao Automatico " + str(testNumber))
        self.driver.find_element_by_id('steps_to_reproduce').send_keys("Teste de passos Automatico " + str(testNumber))
        self.driver.find_element_by_id('additional_info').send_keys("Teste de info. adicional Automatico " + str(testNumber))
        self.driver.find_element_by_id('tag_string').send_keys("TesteDeTag " + str(testNumber))
        self.driver.find_element_by_id('tag_string').send_keys(Keys.RETURN)
    # Esta função  que seleciona a primeira tarefa e apaga ela
    def deletar(self):
        self.driver.find_element_by_xpath(TaskPageElements.APAGAR).click()
        self.driver.find_element_by_xpath(TaskPageElements.CONFIRM_APAGAR).click()
        self.driver.execute_script("alert('TAREFA DELETADA COM SUCESSO!')")
        time.sleep(2)
        self.driver.switch_to.alert.accept()

