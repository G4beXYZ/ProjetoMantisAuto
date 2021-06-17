from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.account_page import AccountPage
from nose.tools import assert_equal,assert_is_not_none,assert_is_not
import time

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
accountPage = AccountPage()

@given(u'que o usuário esteja dentro de Gerenciar Colunas')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)
    dashPage.user_info()
    dashPage.minhaConta()
    accountPage.Gerenciar_Colunas()


@given(u'tenha uma coluna já criada')
def step_impl(context):
    assert_is_not(accountPage.get_allColumns(),"",msg="Não é nulo "+accountPage.get_allColumns())


@then(u'a coluna será copiada para outro projeto')
def step_impl(context):
    accountPage.copiar_coluna()