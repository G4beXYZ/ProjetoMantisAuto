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


@given(u'que o usuário esteja logado')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)


@given(u'esteja na em minha conta')
def step_impl(context):
    dashPage.user_info()
    dashPage.minhaConta()


@given(u'o usuário esteja na aba de Gerenciar Colunas')
def step_impl(context):
    accountPage.Gerenciar_Colunas()


@then(u'ele irá redefinir as configurações das colunas')
def step_impl(context):
    accountPage.ReinicializarColunas()
