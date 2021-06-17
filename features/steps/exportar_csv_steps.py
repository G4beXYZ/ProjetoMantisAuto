from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.task_page import TaskPage
from pages.task_list_page import TaskList ,TaskListElements
from nose.tools import assert_equal,assert_greater
import time

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
taskPage = TaskPage();
taskListPage = TaskList();

@given(u'que o usuário esteja na aba Ver Tarefas')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)
    dashPage.ver_tarefas()


@given(u'tenha uma tarefa criada e disponivel para exportar')
def step_impl(context):
    assert_greater(taskListPage.get_list(), 0)


@then(u'a tarefa será exportada para um arquivo CSV')
def step_impl(context):
    taskListPage.exportar_csv()