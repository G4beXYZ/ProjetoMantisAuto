from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.task_list_page import TaskList, TaskListElements
from nose.tools import assert_equal
import time

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
taskListPage = TaskList()
taskListElements = TaskListElements()

@given(u'que o usuario acesse as tarefas feitas')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)


@given(u'abra a tarefa que deseja alterar')
def step_impl(context):
    dashPage.ver_tarefas()
    taskListPage.select_task_alter()
    if TaskListElements.taskNotFound == True :
        context.scenario.skip(reason="Não possui tarefas alteraveis")
    else:
        pass



@then(u'a Tarefa vai ser alterada')
def step_impl(context):
        idAlterado = int(input("Digite o numero do arquivo de teste >: "))
        taskListPage.preencher_alterado(idAlterado)
