from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.task_page import TaskPage
from pages.task_list_page import TaskList ,TaskListElements
from nose.tools import assert_equal
import time

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
taskPage = TaskPage();
taskListPage = TaskList();
taskListElements = TaskListElements();

@given(u'que a tarefa criada esteja como novo')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)
    dashPage.ver_tarefas()
    taskListPage.select_task()
    if taskListElements.taskNotFound == True:
        context.scenario.skip(reason='Não há tarefas para alterar o status')
    else:
        assert_equal(taskPage.get_status(),'true')


@given(u'o usuário queira mudar o status dela')
def step_impl(context):
    taskPage.mudar_status()


@then(u'o status irá ser atualizado para resolvido')
def step_impl(context):
    taskPage.atualizar_tarefa()
