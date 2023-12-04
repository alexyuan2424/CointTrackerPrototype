# app/data_saver.py
from app import db
from app.models import User, BitcoinAddress, Transaction


class DataRepository:
    def create_user(self, name):
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_id(self, user_id):
        return User.query.get_or_404(user_id)

    def create_bitcoin_address(self, user_id, address_url, final_balance=None, number_of_transactions=None, total_received=None, total_sent=None):
        bitcoin_address = BitcoinAddress(
            user_id=user_id,
            address_url=address_url,
            final_balance=final_balance,
            number_of_transactions=number_of_transactions,
            total_received=total_received,
            total_sent=total_sent
        )
        db.session.add(bitcoin_address)
        db.session.commit()
        return bitcoin_address

    def update_bitcoin_address(self, address_url, final_balance=None, number_of_transactions=None, total_received=None,
                               total_sent=None):
        bitcoin_address = BitcoinAddress.query.filter_by(address_url=address_url).first_or_404()

        if final_balance is not None:
            bitcoin_address.final_balance = final_balance

        if number_of_transactions is not None:
            bitcoin_address.number_of_transactions = number_of_transactions

        if total_received is not None:
            bitcoin_address.total_received = total_received

        if total_sent is not None:
            bitcoin_address.total_sent = total_sent

        db.session.commit()
        return bitcoin_address

    def create_transaction(self, bitcoin_address_id, fee, total_value, balance, transaction_time):
        transaction = Transaction(
            bitcoin_address_id=bitcoin_address_id,
            fee=fee,
            total_value=total_value,
            balance=balance,
            transaction_time=transaction_time
        )
        db.session.add(transaction)
        db.session.commit()
        return transaction

    def get_all_addresses(self):
        addresses = BitcoinAddress.query.all()
        addresses_list = []

        for address in addresses:
            address_info = {'id': address.id, 'address_url': address.address_url, 'user_id': address.user_id}
            addresses_list.append(address_info)

        return addresses_list

    def get_all_addresses_for_user(self, user_id):
        return BitcoinAddress.query.filter_by(user_id=user_id)

    def get_all_transactions_for_address_url(self, address_url):
        transactions = Transaction.query.filter_by(bitcoin_address_id=address_url)
        return transactions

