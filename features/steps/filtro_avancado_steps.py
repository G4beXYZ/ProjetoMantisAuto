from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.account_page import AccountPage
from pages.task_page import TaskPage
from pages.task_list_page import TaskList
from nose.tools import assert_equal,assert_greater
import time

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
accountPage = AccountPage()
taskPage = TaskPage()
taskList = TaskList()


@given(u'que esteja logado no website')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)

@given(u'que o usuário esteja na aba "Ver Tarefas"')
def step_impl(context):
    dashPage.ver_tarefas()
    assert_greater(taskList.get_list(), 0)


@given(u'o usuário clique no menu rapido da lista de filtros')
def step_impl(context):
    taskList.filtro_dropdown()


@then(u'será habilitado o filtro avançado')
def step_impl(context):
    taskList.filtro_avancado()