from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.account_page import AccountPage
from pages.task_page import TaskPage
from nose.tools import assert_equal,assert_greater

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
accountPage = AccountPage()
taskPage = TaskPage()




@given(u'que o usuário está na aba "Token API"')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)
    dashPage.user_info()
    dashPage.minhaConta()
    accountPage.Tokens(uVars.SENHA)


@given(u'que o usuário ja tenha um TokenAPI')
def step_impl(context):
    assert_greater(accountPage.get_tokenList(),0)


@then(u'o TokenAPI previamente criado vai ser revogado')
def step_impl(context):
    accountPage.revogar_token()