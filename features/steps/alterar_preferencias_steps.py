from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.account_page import AccountPage
from pages.task_page import TaskPage
from nose.tools import assert_equal

import time

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
accountPage = AccountPage()
taskPage = TaskPage()

@given(u'que o usuário queira alterar as preferências')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)
    dashPage.user_info()


@given(u'ele esteja na aba de preferências')
def step_impl(context):
    dashPage.minhaConta()
    accountPage.Preferencias()
    assert_equal(accountPage.get_widgetTitle(),"Preferências da Conta")

@then(u'as preferências serão alteradas')
def step_impl(context):
    accountPage.atualizar_Prefencias()



