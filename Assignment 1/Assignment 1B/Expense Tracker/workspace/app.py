from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Transaction

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.get_json()
    transaction = Transaction(amount=data['amount'], category=data['category'], date=data['date'])
    db.session.add(transaction)
    db.session.commit()
    return jsonify(transaction.serialize()), 201

@app.route('/transactions/<int:transaction_id>', methods=['PUT'])
def edit_transaction(transaction_id):
    data = request.get_json()
    transaction = Transaction.query.get(transaction_id)
    transaction.amount = data['amount']
    transaction.category = data['category']
    transaction.date = data['date']
    db.session.commit()
    return jsonify(transaction.serialize()), 200

@app.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    db.session.delete(transaction)
    db.session.commit()
    return '', 204

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([transaction.serialize() for transaction in transactions]), 200

@app.route('/totals', methods=['GET'])
def calculate_totals():
    incomes = Transaction.query.filter(Transaction.amount > 0).all()
    expenses = Transaction.query.filter(Transaction.amount < 0).all()
    total_income = sum(income.amount for income in incomes)
    total_expense = sum(expense.amount for expense in expenses)
    net_balance = total_income + total_expense
    return jsonify({'total_income': total_income, 'total_expense': total_expense, 'net_balance': net_balance}), 200

# def calculate_totals():
#     incomes = Transaction.query.filter(Transaction.amount > 0).all()
#     expenses = Transaction.query.filter(Transaction.amount < 0).all()
#     total_income = sum(income.amount for income in incomes)
#     total_expense = sum(expense.amount for expense in expenses)
#     net_balance = total_income + total_expense
#     return jsonify({'total_income': total_income, 'total_expense': total_expense, 'net_balance': net_balance}), 200


if __name__ == '__main__':
    app.run(debug=True)
