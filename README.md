# ProjetoMantisAuto
Projeto com 30 testes automatizados que visam testar funcionalidades no site MantisBT

<h1> Como Utilizar? </h1>
<b>Utilizando o comando behave </b><br>
<p>Basicamente o behave é o que vai interpretar os steps das features criadas com o código python criado</p>
<p>Então para executar a feature, necessita-se apenas escrever no console o comando igual no exemplo abaixo</p>


```python
  >>> behave -i login.feature
```
<p>o prefixo <b><i>' -i '</i></b> é para executar apenas a feature escolhida</p>

<b>Resultado</b><br>
```cmd
Funcionalidade: login # features/login.feature:2

  @login
  Cenário: realizar login                            # features/login.feature:4
    Dado que acesso o site do Mantis                 # features/steps/login_steps.py:14
    E insiro o valor de usuário no campo             # features/steps/login_steps.py:18
    E insiro o valor de senha no campo               # features/steps/login_steps.py:23
    Então devo vizualizar a dashboard da minha conta # features/steps/login_steps.py:28

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
4 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m6.198s

```
