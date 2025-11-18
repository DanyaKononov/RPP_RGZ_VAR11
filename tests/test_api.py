import pytest
from app import create_app
from app.models import db, User, Resource

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_register(client):
    response = client.post('/register', json={
        'username': 'test',
        'password': 'test',
        'subscription_level': 'basic',
        'account_status': 'active'
    })
    assert response.status_code == 201
