from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from nose.tools import assert_equal

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
@given(u'que o usuário acessou o site')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")


@given(u'inseriu os dados de login')
def step_impl(context):
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)


@given(u'foi parar na página inicial')
def step_impl(context):
    assert_equal(dashPage.get_titulo(),"Minha Visão")


@then(u'será direcionado para a aba “minha conta” onde poderá mudar a senha')
def step_impl(context):
    dashPage.user_info()
    dashPage.minhaConta()
