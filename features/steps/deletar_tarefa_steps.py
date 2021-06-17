from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from nose.tools import assert_equal,assert_greater
from pages.task_list_page import TaskList
from pages.task_page import TaskPage
import time

loginPage = LoginPage()
utils = Utils()
uVars = UtilVars()
dashPage = DashboardPage()
taskList = TaskList()
taskPage = TaskPage()

@given(u'que esteja logado como desenvolvedor')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)
    assert_equal(dashPage.get_cargo(),uVars.CARGO)


@given(u'que tenha tarefas criadas')
def step_impl(context):
    dashPage.ver_tarefas()
    assert_greater(taskList.get_list(),0)

@given(u'o usuário queira deletar alguma delas')
def step_impl(context):
    taskList.select_firstTask()


@then(u'a tarefa será deletada')
def step_impl(context):
    taskPage.deletar()
    time.sleep(5)
    utils.driver.quit()

