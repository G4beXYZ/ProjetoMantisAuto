from behave import given,then
from selenium import webdriver
from utils import Utils, UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from nose.tools import assert_equal
import time

loginPage = LoginPage()
utils = Utils()
uVars = UtilVars()
dashPage = DashboardPage()

@given(u'que o usuário esteja logado no Mantis')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)



@given(u'queira fazer logout')
def step_impl(context):
    dashPage.user_info()


@then(u'o usuário irá fazer logout')
def step_impl(context):
    dashPage.sair()
