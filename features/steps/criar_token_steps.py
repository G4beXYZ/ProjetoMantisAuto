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


@given(u'que o usuário acabou de se logar')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)



@given(u'entrou na parte de "Minha Conta"')
def step_impl(context):
    dashPage.user_info()
    dashPage.minhaConta()

@given(u'foi para a aba de criação de Token API')
def step_impl(context):
    accountPage.Tokens(uVars.SENHA)


@then(u'entrará com um texto para o Token ser criado')
def step_impl(context):
    accountPage.criar_token(input("Nome teste para token : >>> "))