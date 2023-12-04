# app/models.py
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bitcoin_addresses = db.relationship('BitcoinAddress', backref='user', lazy=True)


class BitcoinAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_url = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    final_balance = db.Column(db.Integer)
    number_of_transactions = db.Column(db.Integer)
    total_received = db.Column(db.Integer)
    total_sent = db.Column(db.Integer)

    transactions = db.relationship('Transaction', backref='bitcoin_address', lazy=True)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bitcoin_address_id = db.Column(db.Integer, db.ForeignKey('bitcoin_address.id'), nullable=False)
    fee = db.Column(db.Integer)
    total_value = db.Column(db.Integer)
    balance = db.Column(db.Integer)
    transaction_time = db.Column(db.Integer)
