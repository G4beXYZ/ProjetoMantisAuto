#language: pt
Funcionalidade: Alterar visibilidade de uma tarefa
  Cenário: Alterar se uma tarefa e publica ou privada
    Dado que o usuário está logado na página
    E que o usuário esteja na parte de "Ver Tarefas"
    E e tenha selecionado pelo menos uma tarefa
    Então será alterado a visibilidade da tarefa de público para privado
