# ProjetoMantisAuto
Projeto com 30 testes automatizados que visam testar funcionalidades no site MantisBT

<h1> Como Utilizar? </h1>
<b>Utilizando o comando behave </b><br>
<p></p>

```python
$>>> behave -i login.feature
```

<b>Resultado</b><br>
```cmd
DevTools listening on ws://127.0.0.1:50380/devtools/browser/f666c193-81e7-43b1-aa6e-a98675d8958d
[30420:9816:0617/155333.971:ERROR:device_event_log_impl.cc(214)] [15:53:33.971] Bluetooth: bluetooth_adapter_winrt.cc:1072 Getting Default Adapter failed.
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
