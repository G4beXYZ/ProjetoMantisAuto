from browser import Browser,Keys

# Classe especial para armazenar algumas variáveis com um valor fixo de uma pagina (facilita o acesso)
class AccountPageElement(object):
    WARN = '//*[@id="main-container"]/div/div/div/div/div[4]/p/text()'
    WARN_PHRASE = "Você está visitando uma página segura, e sua sessão expirou. Por favor autentique-se novamente."
    BUTTON_ATUALIZAR_COLUNAS = '//*[@id="manage-columns-form"]/div/div[2]/input'
    BUTTON_COPIAR_COLUNAS_PARA = '//*[@id="manage-columns-copy-form"]/fieldset/input[5]'
    BUTTON_REINCIALIZAR_COLUNAS = '//*[@id="main-container"]/div[2]/div[2]/div/div/div[6]/form/fieldset/input[2]'
    BUTTON_ADICIONAR_PERFIL = '//*[@id="account-profile-form"]/fieldset/div/div[2]/div[2]/input'
    BUTTON_ATUALIZAR_PERFIL = '//*[@id="main-container"]/div[2]/div[2]/div/div/form/div/div[2]/div[2]/input'
    BUTTON_CONFIRMAR_ACAO = '//*[@id="account-profile-update-form"]/div/div[2]/div[2]/input'
    BUTTON_CRIAR_TOKEN = '//*[@id="account-create-api-token-form"]/div/div[2]/div[2]/input'
    PERFIL_PLATAFORMA = 'platform'
    PERFIL_SO = 'os'
    PERFIL_SO_VERSION = 'os-version'

# --------------------------------------------------------------------------------------------------------
# [Classe que herda as condições do script Browser.py, aqui é onde criamos as funções de pesquisa para uma
# página em específico no site do Mantis, no caso desta classe, ela é específica para a
# página MINHA CONTA]
class AccountPage(Browser):

    #[Esta função pega o elemento h4 da pagina MINHA CONTA que no caso seria o título de uma aba, serve para verificar
    #se o programa está seguindo o fluxo certo]
    def get_widgetTitle(self):
        return self.driver.find_element_by_tag_name('h4').text

    # [Esta função é serve para verificar se no campo onde é armazenada todas as colunas na aba "Gerenciar Colunas"
    # possui alguma coluna escrita no campo ou não, a função acaba retornando os valores do campo escolhido
    #  podendo ter dentro dele um valor x de n tamanho ou um valor nulo]
    def get_allColumns(self):
        return self.driver.find_element_by_id('all-columns').text
    # Esta função é serve para verificar se na aba "Perfis" existe algum projeto com que possa ser trabalhado
    def get_projeto(self):
        return self.driver.find_element_by_xpath('//*[@id="manage-columns-copy-form"]/fieldset/select/option[2]').text

    # Esta função é serve para procurar quantos tokens existem e retorna um valor com o total de tokens na tabela
    def get_tokenList(self):
        elements = self.driver.find_elements_by_xpath('//*[@id="api-token-list-div"]/div/div[2]/div/div/table/tbody/tr')
        print("QUANTIDADE DE TOKENS > "+ str(len(elements)))
        return len(elements)
    #Esta função executa a ação de atualizar as prefências
    def atualizar_Prefencias(self):
        self.driver.find_element_by_xpath('//*[@id="account-prefs-update-form"]/fieldset/div/div[2]/div[2]/input[1]').click()
    #Esta função procura pela aba de PREFERÊNCIAS em MINHA CONTA e acessa ela para executar outras funções depois
    def Preferencias(self):
        self.driver.find_element_by_xpath('//*[@id="main-container"]/div[2]/div[2]/div/ul/li[2]/a').click()

    # Esta função procura pela aba de GERENCIAR COLUNAS em MINHA CONTA e acessa ela para executar outras funções depois
    def Gerenciar_Colunas(self):
        self.driver.find_element_by_xpath('//*[@id="main-container"]/div[2]/div[2]/div/ul/li[3]/a').click()

    # Esta função procura pela aba de PERFIS em MINHA CONTA e acessa ela para executar outras funções depois
    def Perfis(self):
        self.driver.find_element_by_xpath('//*[@id="main-container"]/div[2]/div[2]/div/ul/li[4]/a').click()

    # Esta função procura pela aba de TOKENS API em MINHA CONTA e acessa ela para executar outras funções depois
    def Tokens(self,userPass):
        self.driver.find_element_by_xpath('//*[@id="main-container"]/div[2]/div[2]/div/ul/li[5]/a').click()
        if AccountPageElement.WARN[0] == AccountPageElement.WARN_PHRASE:
            self.driver.find_element_by_id("password").send_keys(userPass)
            self.driver.find_element_by_id("password").send_keys(Keys.RETURN)
        else:
            pass

    # [Esta função é serve para criar um Token com um nome escolhido por input para facilitar o teste, e depois ele
    # retorna no console o token criado]
    def criar_token(self,nomeToken):
        self.driver.find_element_by_id('token_name').send_keys(nomeToken)
        self.driver.find_element_by_xpath(AccountPageElement.BUTTON_CRIAR_TOKEN).click()
        print("TOKEN CRIADO ==>["+self.driver.find_element_by_class_name('well').text+"]")
        print("ATENÇÃO: Guarde ele em um lugar seguro!")

    # [Esta função é serve para revogar um token criado, onde a função pega o primeiro da lista dos tokens criados
    # e revoga ele]
    def revogar_token(self):
        self.driver.find_element_by_xpath('//*[@id="revoke-api-token-form"]/fieldset/input[3]').click()

    # Esta função é serve para atualizar as colunas na aba "Gerenciar Colunas"

    def atualizar_coluna(self):
        self.driver.find_element_by_xpath(AccountPageElement.BUTTON_ATUALIZAR_COLUNAS).click()

    # Esta função é serve para reinicializar as colunas na aba "Gerenciar Colunas"
    def ReinicializarColunas(self):
        self.driver.find_element_by_xpath(AccountPageElement.BUTTON_REINCIALIZAR_COLUNAS).click()

    # Esta função é serve para copiar as colunas na aba "Gerenciar Colunas" para um outro projeto
    def copiar_coluna(self):
        self.driver.find_element_by_xpath(AccountPageElement.BUTTON_COPIAR_COLUNAS_PARA).click()

    # Esta função é serve para preencher um perfil com valores de teste na aba "Perfis"
    def preencher_perfil(self,testData):
        self.driver.find_element_by_id(AccountPageElement.PERFIL_PLATAFORMA).send_keys(testData)
        self.driver.find_element_by_id(AccountPageElement.PERFIL_SO).send_keys(testData)
        self.driver.find_element_by_id(AccountPageElement.PERFIL_SO_VERSION).send_keys(testData)

    # Esta função é serve confirmar o preenchimento do perfil na aba "Perfis"
    def adicionar_perfil(self):
        self.driver.find_element_by_xpath(AccountPageElement.BUTTON_ADICIONAR_PERFIL).click()

    # Esta função é serve para editar um perfil criado na aba "Perfis"
    def editar_perfil(self):
        #fazendo a ação de clicar no botão radial 'editar' e depois confirmando a ação com um outro botão
        self.driver.execute_script("document.getElementById('action-edit').click()")
        self.driver.find_element_by_xpath(AccountPageElement.BUTTON_CONFIRMAR_ACAO).click()

        # Escrevendo valores editados nos campos já predefinidos
        self.driver.find_element_by_name('platform').send_keys(" [EDITADO]")
        self.driver.find_element_by_name('os').send_keys(" [EDITADO]")
        self.driver.find_element_by_name('os_build').send_keys("[EDITADO]")
        self.driver.find_element_by_xpath(AccountPageElement.BUTTON_ATUALIZAR_PERFIL).click()

    # Esta função é serve para tornar um perfil criado como padrão de uso na aba "Perfis"
    def tornar_padrao(self):
        self.driver.execute_script("document.getElementById('action-default').click()")
        self.driver.find_element_by_xpath(AccountPageElement.BUTTON_CONFIRMAR_ACAO).click()
    # Esta função é serve para excluir um perfil criado na aba "Perfis"
    def excluir_perfil(self):
        self.driver.execute_script("document.getElementById('action-delete').click()")
        self.driver.find_element_by_xpath(AccountPageElement.BUTTON_CONFIRMAR_ACAO).click()

    # Esta função é serve para selecionar o primeiro perfil da lista dos perfis criados na aba "Perfis"
    def selecionar_perfil(self):
        self.driver.find_element_by_xpath('//*[@id="select-profile"]/option[2]').click()