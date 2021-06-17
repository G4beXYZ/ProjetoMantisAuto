from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.account_page import AccountPage
from nose.tools import assert_equal
import time
utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
accountPage = AccountPage()
@given(u'que o usuario acabou de se logar')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)


@given(u'deseja criar um Token API')
def step_impl(context):
    dashPage.user_info()


@given(u'est na dashboard inicial')
def step_impl(context):
    assert_equal(dashPage.get_nome(), uVars.USUARIO_COMPLETO)
    assert_equal(dashPage.get_titulo(), "Minha Visão")


@then(u'sera direcionado para a aba de criação de Token API')
def step_impl(context):
    dashPage.minhaConta()
    accountPage.Tokens(uVars.SENHA)
    assert_equal(accountPage.get_widgetTitle(),"Criar token API")

