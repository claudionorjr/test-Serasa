# Documentação

## Executando o programa em Linux/windows

### LINUX
***OBS***: Com MakeFile:

- No terminal com o diretório do programa setado:

* `help` para mais informações.
* `make installvirtualenv` serve para instalar o virtualenv.
* `ambvir`serve para criar um ambiente virtual.
* `start` serve para iniciar seu ambiente virtual. 
* `install` serve para instalar todas as dependências necessárias. 
* `run` executa o arquivo principal.
* `test` executa os testes unitários.


***OBS***: Direto no terminal:

* `sudo apt install virtualenv` (se ainda não tiver instalado)
* `virtualenv .ambvir --python=python3.7` (instalar o virtualenv `.ambvir`)
* `source .ambvir/bin/activate` (iniciar seu ambiente virtual)
* `pip install -r requirements/base.txt` (instalar todas as dependências necessárias)
* `python app.py` (executa o arquivo principal)
* `pytest -v` (executa os testes unitários)


### WINDOWS

- No terminal com o diretório do programa setado:

* `pip install virtualenv` (se ainda não tiver instalado)
* `virtualenv .ambvir --python=python3.7` (instalar o virtualenv `.ambvir`)
* `.\.ambvir\Scripts\activate` (iniciar seu ambiente virtual)
* `pip install -r requirements\base.txt` (instalar todas as dependências necessárias)
* `python app.py` (executa o arquivo principal)
* `pytest -v` (executa os testes unitários)


## Sobre anexar o arquivo

- Para o programa ler os dados a ser enviados, é necessário anexar um arquivo de estrutura `JSON`.
- O arquivo modelo escontra-se no diretório raiz do sistema, chamado `archive.json`.

### Modelo
```python
{
    "invoices": 2,
    "debits": 0
}
```
* invoices: Receberá a quantidade de notas fiscais.
* debits: Receberá a quantidade de débitos.


## Rotas 

### Usuário não autenticado
* url `http://127.0.0.1:5000/`

```python
# Login
@app.route("/", methods=["GET","POST"])

# Register
@app.route("/register", methods=["GET","POST"])
```

### Usuário deve estar autenticado
```python
# Home
@app.route("/current_user")

# Formulário para enviar arquivo na página Home
# ID da empresa cujo o formulário fica na mesma linha da tabela!
@app.route('/current_user/uploader/<int:id>', methods = ['GET', 'POST'])

# Sobre a conta do usuário
@app.route("/current_user/account")

# Tela de confirmação antes de deletar o usuário
@app.route("/current_user/delete")

# Deleta o usuário logado
# ID do usuário logado!
@app.route("/current_user/delete/<int:id>")

# Deleta automaticamente a empresa selecionada
# ID da empresa cujo o formulário fica na mesma linha da tabela!
@app.route("/current_user/company/delete/<int:id>")

# Logout do usuário autenticado
@app.route("/logout")

# Formulário para criar nova empresa na página Home
@app.route("/current_user/create_company/new", methods=["GET","POST"])
```


## Framework e bibliotecas adicionais

* Flask
* Flask-SQLAlchemy
* python-dotenv
* flask-wtf
* bootstrap-flask
* flask-login
* pytest

## Resultado dos testes

´´´
=================================== test session starts ===================================
platform win32 -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1 -- c:\users\test-serasa\.ambvir\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\test-Serasa
collected 12 items

tests/test_app.py::test_login_if_return_200 PASSED---------------------------------------------[  8%]
tests/test_app.py::test_register_if_return_200 PASSED------------------------------------------[ 16%]
tests/test_app.py::test_if_have_registrar PASSED-----------------------------------------------[ 25%]
tests/test_app.py::test_if_have_logar PASSED---------------------------------------------------[ 33%]
tests/test_app.py::test_register_user PASSED---------------------------------------------------[ 41%]
tests/test_app.py::test_login_user PASSED------------------------------------------------------[ 50%]
tests/test_app.py::test_if_route_home_is_blocked PASSED----------------------------------------[ 58%] 
tests/test_app.py::test_if_route_account_is_blocked PASSED-------------------------------------[ 66%] 
tests/test_app.py::test_if_route_confirme_delete_is_blocked PASSED-----------------------------[ 75%] 
tests/test_app.py::test_if_route_user_delete_is_blocked PASSED---------------------------------[ 83%] 
tests/test_app.py::test_if_route_company_delete_is_blocked PASSED------------------------------[ 91%] 
tests/test_app.py::test_if_route_new_company_is_blocked PASSED---------------------------------[100%] 

=================================== 12 passed in 1.94s ===================================
```