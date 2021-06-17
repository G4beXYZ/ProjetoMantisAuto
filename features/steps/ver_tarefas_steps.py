from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from nose.tools import assert_equal
import time

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()

@given(u'que o usuário tenha acesso a sua conta')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)

@given(u'conseguiu logar com sucesso')
def step_impl(context):
    assert_equal(dashPage.get_nome(),uVars.USUARIO_COMPLETO)


@given(u'entrou na pagina inicial “Minha visão”')
def step_impl(context):
    assert_equal(dashPage.get_titulo(),"Minha Visão")


@then(u'ir para a aba “Ver minhas tarefas”')
def step_impl(context):
    dashPage.ver_tarefas()

