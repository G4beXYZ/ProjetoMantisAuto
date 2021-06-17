from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from nose.tools import assert_equal,assert_greater
from pages.task_page import TaskPage
from pages.task_list_page import TaskList ,TaskListElements
import time

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
taskPage = TaskPage();
taskListPage = TaskList();

@given(u'que o usuário esteja em ver tarefas')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)
    dashPage.ver_tarefas()


@given(u'tenha tarefas já criadas e disponiveis')
def step_impl(context):
    assert_greater(taskListPage.get_list(), 0)


@then(u'as tarefas serão imprimidas')
def step_impl(context):
    taskListPage.imprimir_tarefas()