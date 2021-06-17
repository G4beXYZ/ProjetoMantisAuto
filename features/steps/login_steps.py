from behave import given,then
from selenium import webdriver
from utils import Utils ,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from nose.tools import assert_equal
import time

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()

@given(u'que acesso o site do Mantis')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")

@given(u'insiro o valor de usuário no campo')
def step_impl(context):
    loginPage.inserir_usuario(uVars.USUARIO)


@given(u'insiro o valor de senha no campo')
def step_impl(context):
    loginPage.inserir_senha(uVars.SENHA)


@then(u'devo vizualizar a dashboard da minha conta')
def step_impl(context):
    assert_equal(dashPage.get_nome(),uVars.USUARIO_COMPLETO)
    assert_equal(dashPage.get_titulo(),"Minha Visão")
    dashPage.show_usuario(uVars.USUARIO)

