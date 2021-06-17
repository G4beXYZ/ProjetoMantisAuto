from browser import Browser,Keys
import time
from selenium.common.exceptions import NoSuchElementException


# Classe especial para armazenar algumas variáveis com um valor fixo de uma pagina (facilita o acesso)
class TaskListElements(object):
    FIRST_TASK = '//*[@id="buglist"]/tbody/tr[1]/td[11]'
    FIRST_TASK_ID = '//*[@id="buglist"]/tbody/tr[1]/td[4]/a'
    BUTTON_REDEFINIR_FILTRO = '//*[@id="filter"]/div[2]/div/div/div/div/a[1]'
    BUTTON_SALVAR_FILTRO = '//*[@id="filter"]/div[2]/div/div/div/div/a[2]'
    BUTTON_APLICAR_FILTRO = '//*[@id="filters_form_open"]/div[2]/div/div/input[2]'
    BUTTON_IMPRIMIR_TAREFAS = '//*[@id="bug_action"]/div/div[2]/div[1]/div/div[1]/a[1]'
    BUTTON_EXPORTAR_CSV = '//*[@id="bug_action"]/div/div[2]/div[1]/div/div[1]/a[2]'
    BUTTON_EXPORTAR_EXCEL = '//*[@id="bug_action"]/div/div[2]/div[1]/div/div[1]/a[3]'
    BUTTON_CONFIRM_VISIBILIDADE = '//*[@id="action-group-div"]/form/div/div[2]/div[2]/input'
    IMPRIMIR_WORD = '/html/body/form[1]/table/tbody/tr/td/a[1]'
    IMPRIMIR_WEB = '/html/body/form[1]/table/tbody/tr/td/a[2]'
    FILTRO_AVANCADO = '//*[@id="filter"]/div[1]/div[1]/div/ul/li[1]/a'
    taskNotFound = False
# --------------------------------------------------------------------------------------------------------
# [Classe que herda as condições do script Browser.py, aqui é onde criamos as funções de pesquisa para uma
# página em específico no site do Mantis, no caso desta classe, ela é específica para a lista de tarefas
# na aba "Ver Tarefas"]
class TaskList(Browser):


    # [Esta função pega o elemento h4 da pagina ATUALIZAR INFORMAÇÕES DE TAREFA que no caso
    # seria o título de uma aba, serve para verificar se o programa está seguindo o fluxo certo]
    def get_widgetTitle(self):
        return self.driver.find_element_by_tag_name('h4').text

    #Esta função pega os elementos de uma tabela (tbody) e retorna a length dela (usada para metodos de comparação)
    def get_list(self):
        elements = self.driver.find_elements_by_xpath('//*[@id="buglist"]/tbody/tr')
        if len(elements) == 1:
            print(">>>>",len(elements),"TAREFA ENCONTRADA <<<<")
        elif len(elements) > 1:
            print(">>>>", len(elements), "TAREFAS ENCONTRADAS <<<<")
        else:
            print(">>>>", len(elements), "NENHUMA TAREFA ENCONTRADA <<<<")
        return len(elements)

    # Esta marca a caixa de seleção da primeira tarefa encontrada na lista de tarefas em "Ver Tarefas"
    def mark_task_box(self):
        box = self.driver.find_element_by_xpath('//*[@id="buglist"]/tbody/tr[1]/td[1]/div/label/span')
        self.driver.execute_script("arguments[0].click()",box)
        self.driver.find_element_by_xpath('//*[@id="bug_action"]/div/div[2]/div[2]/div[2]/div[1]/select/option[11]').click()

    # Esta função clica no botão "OK" assim confirmando a execução de uma modificação rápida em um elemento
    # selecionado da lista. O nome "variant" é dado pois existe um método longo de editar uma tarefa, então este
    # seria sua variante
    def variant_select(self):
        self.driver.find_element_by_xpath('//*[@id="bug_action"]/div/div[2]/div[2]/div[2]/div[1]/input').click()

    # Esta função altera a visibilidade de uma tarefa de "Público" para "Privado"
    def alterar_visibilidade(self):
        self.driver.find_element_by_xpath('//*[@id="action-group-div"]/form/div/div[2]/div[1]/div/table/tbody/tr[1]/td/select/option[2]').click()
        self.driver.find_element_by_xpath(TaskListElements.BUTTON_CONFIRM_VISIBILIDADE).click()


    #Esta função seleciona a primeira tarefa encontrada na lista da aba "Tarefas"
    def select_firstTask(self):
        self.driver.find_element_by_xpath(TaskListElements.FIRST_TASK_ID).click()

    # Esta função procura por tarefas não resolvidas e clica em alguma disponível para acessar a pagina de alterar
    def select_task_alter(self):
        elements = self.driver.find_elements_by_xpath('//*[@id="buglist"]/tbody/tr')
        count = 0
        try:
            while (count < len(elements)):
                for row in elements:
                    count = count + 1
                    if row.find_element_by_class_name('column-edit').text != " ":
                        alteraveis = row.find_elements_by_class_name('column-edit')
                        print(row.find_element_by_class_name('column-id').text + ' [ALTERÁVEL]\n')
                        for alter in alteraveis:
                            alter.click()
                            return
                    elif row.find_element_by_class_name('column-edit').text == " ":
                        print(row.find_element_by_class_name('column-id').text + ' ......[NÃO ALTERÁVEL]\n')
                        if count >= len(elements):
                            self.driver.execute_script("alert('NÃO HÁ TAREFAS PARA SEREM ALTERADAS')")
                            time.sleep(2)
                            self.driver.switch_to.alert.accept()
                            self.driver.execute_script("alert('VERIFIQUE SE A LISTA POSSUI ITENS ALTERAVEIS')")
                            time.sleep(2)
                            self.driver.switch_to.alert.accept()
                            self.driver.execute_script("alert('PULANDO TESTES')")
                            time.sleep(1)
                            self.driver.switch_to.alert.accept()
                            TaskListElements.taskNotFound = True
                        else:
                            pass
        except NoSuchElementException as e:
            return e

    # Parecida com a função acima, esta daqui procura por tarefas não resolvidas e entra na página principal dela para
    # que assim possam ser executadas novas funções para modificar algo na página da tarefa escolhida
    def select_task(self):
        elements = self.driver.find_elements_by_xpath('//*[@id="buglist"]/tbody/tr')
        count = 0
        try:
            while (count < len(elements)):
                for row in elements:
                    count = count + 1
                    print(str(len(elements)) + "/" + str(count) + ' ID da TAREFA: ' + row.find_element_by_class_name(
                        'column-id').text + ' [TODOS]\n')
                    if row.find_element_by_class_name('column-edit').text != " ":
                        print(row.find_element_by_class_name('column-id').text + '==>[ATRIBUIDO]<==\n')
                        atribuidos = row.find_elements_by_class_name('column-id')
                        for atri in atribuidos:
                            atri.click()
                            return
                    elif row.find_element_by_class_name('column-edit').text == " ":
                        if count >= len(elements):
                            self.driver.execute_script("alert('NÃO HÁ TAREFAS ATRIBUÍDAS OU TODAS FORAM RESOLVIDAS!')")
                            time.sleep(2)
                            self.driver.switch_to.alert.accept()
                            self.driver.execute_script("alert('REPITA O TESTE COM TAREFAS ATRIBUÍDAS NA LISTA')")
                            time.sleep(2)
                            self.driver.switch_to.alert.accept()
                            self.driver.execute_script("alert('PULANDO TESTES')")
                            time.sleep(1)
                            self.driver.switch_to.alert.accept()
                            TaskListElements.taskNotFound = True
                        else:
                            pass
        except NoSuchElementException as e:
               return e



    # [Esta função preenche os campos do formulário de alteração de uma tarefa
    # com dados parecidos com os encontrados no script task_page.py, porém
    # aqui nós marcamos na string com um [ALTERADO] ao lado]
    def preencher_alterado(self,numeroAlterado):
        self.driver.find_element_by_xpath('//*[@id="reproducibility"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="severity"]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="priority"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="handler_id"]/option[3]').click()
        self.driver.find_element_by_id('summary').clear()
        self.driver.find_element_by_id('summary').send_keys("Teste de resumo Automatico [ALTERADO] " + str(numeroAlterado))
        self.driver.find_element_by_id('description').clear()
        self.driver.find_element_by_id('description').send_keys("Teste de descricao Automatico [ALTERADO] " + str(numeroAlterado))
        self.driver.find_element_by_id('steps_to_reproduce').clear()
        self.driver.find_element_by_id('steps_to_reproduce').send_keys("Teste de passos Automatico [ALTERADO] " + str(numeroAlterado))
        self.driver.find_element_by_id('additional_information').clear()
        self.driver.find_element_by_id('additional_information').send_keys("Teste de info. adicional Automatico [ALTERADO] " + str(numeroAlterado))
        self.driver.find_element_by_id('bugnote_text').send_keys("[ESTE ARQUIVO FOI ALTERADO AUTOMATICAMENTE] " + str(numeroAlterado))
        self.driver.find_element_by_xpath('//*[@id="update_bug_form"]/div/div[3]/input').click()

    # Esta função testa o botão de aplicar filtros na aba "Ver Tarefas"
    def aplicar_filtro(self):
        self.driver.find_element_by_xpath(TaskListElements.BUTTON_APLICAR_FILTRO).click()

    # Esta função testa o botão de redefinir filtros na aba "Ver Tarefas"
    def redefinir_filtro(self):
        self.driver.find_element_by_xpath(TaskListElements.BUTTON_REDEFINIR_FILTRO).click()

    # Esta função testa o botão de salvar filtros na aba "Ver Tarefas"
    def salvar_filtro(self):
        self.driver.find_element_by_xpath(TaskListElements.BUTTON_SALVAR_FILTRO).click()

    # Esta função testa a parte de imprimir tarefas, onde o resultado é tanto um documento word
    # quanto uma exibição numa pagina separada na web, já que nessa função ele executa ambos
    def imprimir_tarefas(self):
        self.driver.find_element_by_xpath(TaskListElements.BUTTON_IMPRIMIR_TAREFAS).click()
        self.driver.find_element_by_xpath(TaskListElements.IMPRIMIR_WORD).click()
        self.driver.find_element_by_xpath(TaskListElements.IMPRIMIR_WEB).click()

    # Esta função testa a parte de exportar tarefas, onde ela acaba sendo exportada para um arquivo .xml
    # Nota: O Webdrive do chrome considera o export desse arquivo como uma ameaça, porém é apenas um falso-positivo
    def exportar_excel(self):
        self.driver.find_element_by_xpath(TaskListElements.BUTTON_EXPORTAR_EXCEL).click()

    # Esta função testa a parte de exportar tarefas, onde ela acaba sendo exportada para um arquivo .csv
    def exportar_csv(self):
        self.driver.find_element_by_xpath(TaskListElements.BUTTON_EXPORTAR_CSV).click()

    # Esta função expande o menu de dropdown que tem na janela dos Filtros no canto superior direito
    def filtro_dropdown(self):
        self.driver.find_element_by_xpath('//*[@id="filter"]/div[1]/div[1]/div/a').click()

    # Esta função habilita e desabilita o filtro de pesquisa avançado pelo menu de dropdown (visto na função anterior)
    def filtro_avancado(self):
        print(self.driver.find_element_by_xpath(TaskListElements.FILTRO_AVANCADO).text)
        if self.driver.find_element_by_xpath(TaskListElements.FILTRO_AVANCADO).text == "  Filtros Simples":
            self.driver.find_element_by_xpath(TaskListElements.FILTRO_AVANCADO).click()
        elif self.driver.find_element_by_xpath(TaskListElements.FILTRO_AVANCADO).text == "  Filtros Avançados":
            print('Já estava Habilitado')
            print('Desabilitando ....')
            self.driver.find_element_by_xpath(TaskListElements.FILTRO_AVANCADO).click()
    # Esta função cria um link permanente para o filtro predefinido por usuários, e ela da um output no console
    # com o link permanente à mostra
    def link_permanente(self):
        self.driver.find_element_by_xpath('//*[@id="filter"]/div[1]/div[1]/div/ul/li[2]/a').click()
        print("\n\nLINK GERADO: \n>>> "+self.driver.find_element_by_xpath('//*[@id="main-container"]/div[2]/div[2]/div/div/p[2]/a').text + " <<< \n")

