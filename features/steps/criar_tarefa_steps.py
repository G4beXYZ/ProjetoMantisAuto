from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.task_page import TaskPage
from nose.tools import assert_equal
import time

loginPage = LoginPage()
utils = Utils()
uVars = UtilVars()
dashPage = DashboardPage()
taskPage = TaskPage()

@given(u'que esteja logado como usuário/desenvolvedor')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)
    assert_equal(dashPage.get_cargo(),uVars.CARGO)


@given(u'esteja na parte de criar Tarefa')
def step_impl(context):
    dashPage.criar_tarefa()


@given(u'preencha o formulário com informações validas')
def step_impl(context):
    testeId = int(input("Digite o numero do arquivo de teste >: "))
    taskPage.preencher(testeId)
    time.sleep(3)

@then(u'a tarefa ira ser criada')
def step_impl(context):
    assert_equal(taskPage.get_state(),"atribuído")
