from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.changelog_page import ChangeLog
from nose.tools import assert_equal
import time

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
changesPage = ChangeLog()

@given(u'que o usuário queira ver as mudanças')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)

@given(u'esteja na aba de Registro de Mudanças')
def step_impl(context):
    dashPage.registro_mudanca()


@then(u'o usuário irá ver as mudanças')
def step_impl(context):
    assert_equal(changesPage.get_lead(),"Não há informações disponíveis sobre registros de mudanças")
