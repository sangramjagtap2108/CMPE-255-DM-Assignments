import pytest
from app import app, db
from models import Transaction
from datetime import datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_add_transaction(client):
    response = client.post('/transactions', json={'amount': 1000, 'category': 'Salary', 'date': datetime.now().isoformat()})
    assert response.status_code == 201
    data = response.get_json()
    assert data['amount'] == 1000
    assert data['category'] == 'Salary'

def test_edit_transaction(client):
    transaction = Transaction(amount=1000, category='Salary', date=datetime.now())
    db.session.add(transaction)
    db.session.commit()
    response = client.put(f'/transactions/{transaction.id}', json={'amount': 2000, 'category': 'Salary', 'date': datetime.now().isoformat()})
    assert response.status_code == 200
    data = response.get_json()
    assert data['amount'] == 2000

def test_delete_transaction(client):
    transaction = Transaction(amount=1000, category='Salary', date=datetime.now())
    db.session.add(transaction)
    db.session.commit()
    response = client.delete(f'/transactions/{transaction.id}')
    assert response.status_code == 204

def test_get_transactions(client):
    transaction1 = Transaction(amount=1000, category='Salary', date=datetime.now())
    transaction2 = Transaction(amount=-500, category='Rent', date=datetime.now())
    db.session.add(transaction1)
    db.session.add(transaction2)
    db.session.commit()
    response = client.get('/transactions')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2

def test_calculate_totals(client):
    transaction1 = Transaction(amount=1000, category='Salary', date=datetime.now())
    transaction2 = Transaction(amount=-500, category='Rent', date=datetime.now())
    db.session.add(transaction1)
    db.session.add(transaction2)
    db.session.commit()
    response = client.get('/totals')
    assert response.status_code == 200
    data = response.get_json()
    assert data['total_income'] == 1000
    assert data['total_expense'] == -500
    assert data['net_balance'] == 500
