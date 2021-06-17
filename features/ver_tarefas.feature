#language: pt
Funcionalidade: Ir para a área de “Ver tarefas”
@vertarefas
  Cenário: Ir automaticamente para a aba de “Ver tarefas”
    Dado que o usuário tenha acesso a sua conta
    E conseguiu logar com sucesso
    E entrou na pagina inicial “Minha visão”
    Então ir para a aba “Ver minhas tarefas”
