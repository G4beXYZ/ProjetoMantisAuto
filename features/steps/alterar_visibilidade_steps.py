from behave import given,then
from selenium import webdriver
from utils import Utils,UtilVars
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.task_page import TaskPage
from pages.task_list_page import TaskList ,TaskListElements
from nose.tools import assert_equal,assert_greater
import time

utils = Utils()
uVars = UtilVars()
loginPage = LoginPage()
dashPage = DashboardPage()
taskPage = TaskPage();
taskListPage = TaskList();

@given(u'que o usuário está logado na página')
def step_impl(context):
    utils.entrar("https://mantis.saojudas.base2.com.br/")
    loginPage.inserir_usuario(uVars.USUARIO)
    loginPage.inserir_senha(uVars.SENHA)


@given(u'que o usuário esteja na parte de "Ver Tarefas"')
def step_impl(context):
    dashPage.ver_tarefas()


@given(u'e tenha selecionado pelo menos uma tarefa')
def step_impl(context):
   taskListPage.get_list()
   taskListPage.mark_task_box()
   taskListPage.variant_select()



@then(u'será alterado a visibilidade da tarefa de público para privado')
def step_impl(context):
    taskListPage.alterar_visibilidade()