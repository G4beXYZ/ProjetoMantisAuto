from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.account_page import AccountPage
from pages.task_page import TaskPage
from nose.tools import assert_equal

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
accountPage = AccountPage()
taskPage = TaskPage()


@given(u'que ja tenha um perfil criado')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)
    dashPage.user_info()
    dashPage.minhaConta()


@given(u'esteja dentro da aba de Perfis')
def step_impl(context):
    accountPage.Perfis()


@given(u'o perfil criado esteja selecionado')
def step_impl(context):
    accountPage.selecionar_perfil()


@then(u'o perfil criado sera apagado')
def step_impl(context):
    accountPage.excluir_perfil()