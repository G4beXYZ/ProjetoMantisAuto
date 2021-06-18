# ProjetoMantisAuto
Projeto com 30 testes automatizados que visam testar funcionalidades no site MantisBT

<h1> Configurações Iniciais </h1>
<h3>Instalando os Requisitos (requirements.txt)</h3>

```python
  >>> pip install -r requirements.txt  
```

  
 ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)
 ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)
 ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)
 ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)
 
 ## IMPORTANTE (CONFIGURAÇÃO DO USUÁRIO)
 
   <h3> Algumas configurações precisam ser feitas no arquivo "utils.py" <br> Veja como configurar logo abaixo 🠓 </h3>
                                                                                                              
   <div><i>Aqui como vocês podem ver, as variáveis do script estão com valores "placeholder".Caso você possua uma conta no MantisBT
   basta colocar o seus dados no lugar dos valores "placeholder"</i> </div>
   
   ### Exemplo:
   
   ```python
    class UtilVars(object):
        USUARIO = 'INSIRA_USUARIO_AQUI'
        SENHA = 'INSIRA_SENHA_AQUI'
        USUARIO_COMPLETO = 'NOME_PAGINA_PRINCIPAL'
        CARGO = 'CARGO_AQUI'

   ```
   
   ### Resultado esperado:
   <p>aqui seria como deve-se preencher os campos</p>
   
   ```python
    class UtilVars(object):
        USUARIO = 'meuUsuario'
        SENHA = 'minhasenhaMantis123'
        USUARIO_COMPLETO = 'meuUsuario ( Meu nome Completo )'
        CARGO = 'meuCargoLegal'

   ```
   
   ### Sobre o USUARIO_COMPLETO:
   <p>Para obter esse valor da forma correta,basta pegar o título que mostra na página principal</p>
   
   #### Exemplo:
   <p><i>Esse nome é encontrado logo no canto superior esquerdo na página incial (Também conhecido como "Minha Visão")</i></p>
  
   <img src=https://user-images.githubusercontent.com/62225558/122469275-243c3600-cf93-11eb-8105-3efcb682f189.png>
   
   #### - ATENÇÃO: OS VALORES DAS VARIÁVEIS PRECISAM ESTAR ESCRITAS DO MESMO JEITO DOS TEXTOS ENCONTRADOS NO SITE -
   
   ## O que fazer após isso?
   <p>Bom...Se você chegou até aqui colocando as variávies no lugar certo e do jeito certo então...<br>
      Meus parabéns você concluiu a configuração tanto da sua conta do MantisBT quanto do "utils.py"
  </p>
   <h2 align="center">⭐⭐Sua etapa de configuração terminou!⭐⭐</h2>
   <h3 align="center">⭐⭐Agora basta ver como utilizar os comandos nos próximos tópicos!⭐⭐</h3>
 
 ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)
 ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)
 ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)
 ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)
 
<h1> Como Utilizar? </h1>

<h3>Utilizando o comando 'Behave'</h3>
<p>Basicamente o behave é o que vai interpretar os steps das features criadas com o código python.<br> 
  Então para executar a feature, necessita-se apenas escrever no console o comando igual no exemplo abaixo
</p>

```python
  >>> behave -i login.feature
```
<p><i>[o prefixo <b><i>' -i '</i></b> é para executar apenas a feature escolhida / um cenário específico]</i></p>

<h5>🔵<i>Documentação completa disponível neste PDF oficial do Behave: https://buildmedia.readthedocs.org/media/pdf/behave/latest/behave.pdf</i></h5>

<h3>Resultado</h3><br>

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
