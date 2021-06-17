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


@given(u'que o usuário esteja em Minha conta')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)
    dashPage.user_info()
    dashPage.minhaConta()

@given(u'esteja na aba de Perfis')
def step_impl(context):
    accountPage.Perfis()


@then(u'será adicionado um novo perfil')
def step_impl(context):
    accountPage.preencher_perfil(input("Insira dados de teste aqui : >>> "))
    accountPage.adicionar_perfil()
