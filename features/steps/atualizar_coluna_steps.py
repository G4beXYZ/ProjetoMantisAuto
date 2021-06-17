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

@given(u'que o usuário esteja em Gerenciar Colunas')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)
    dashPage.user_info()
    dashPage.minhaConta()
    accountPage.Gerenciar_Colunas()


@given(u'tenha um projeto criado')
def step_impl(context):
    assert_equal(accountPage.get_projeto(),'Grupo2')


@then(u'a Coluna desse projeto será atualizada')
def step_impl(context):
    accountPage.atualizar_coluna()