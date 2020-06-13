import pytest
from src.main import create_app
from src.models.user import UserModel
from data.sql_alchemy import database as db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "123456"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
    app.config["WTF_CSRF_ANABLED"] = False

    context = app.app_context()
    context.push()
    db.create_all()

    yield app.test_client()

    db.session.remove()
    db.drop_all()
    context.pop()

daties_register = { "name": "Testando", "email": "joao@gmail.com", "password": "123546"}
daties_login = { "email": "joao@gmail.com", "password": "123546"}

def register(client):
    action = client.post("/register", data=daties_register, follow_redirects=True)
    return action

def login(client):
    action = client.post("/", data=daties_login, follow_redirects=True)
    return action

def test_login_if_return_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_register_if_return_200(client):
    response = client.get("/register")
    assert response.status_code == 200

def test_if_have_registrar(client):
    response = client.get("/")
    assert "Registrar" in response.get_data(as_text=True)

def test_if_have_logar(client):
    response = client.get("/")
    assert "Logar" in response.get_data(as_text=True)

def test_register_user(client):
    response = register(client)
    assert "Testando" in response.get_data(as_text=True)

def test_login_user(client):
    register(client)
    response = login(client)
    assert response.status_code == 200

def test_if_route_home_is_blocked(client):
    response = client.get("/current_user")
    assert response.status_code == 401

def test_if_route_account_is_blocked(client):
    response = client.get("/current_user/account")
    assert response.status_code == 401

def test_if_route_confirme_delete_is_blocked(client):
    response = client.get("/current_user/delete")
    assert response.status_code == 401

def test_if_route_user_delete_is_blocked(client):
    response = client.get("/current_user/delete/1")
    assert response.status_code == 401

def test_if_route_company_delete_is_blocked(client):
    response = client.get("/current_user/company/delete/1")
    assert response.status_code == 401

def test_if_route_new_company_is_blocked(client):
    response = client.get("/current_user/create_company/new")
    assert response.status_code == 401
