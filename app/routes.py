from flask import request
from app import app
from app.data_repository import DataRepository
from app.sync_wallet_data import SyncWalletData

data_repository = DataRepository()
sync_wallet_data = SyncWalletData()


@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    new_user = data_repository.create_user(name=user_data['name'])
    return {'message': 'User created successfully', 'user_id': new_user.id}


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = data_repository.get_user_by_id(user_id)
    return {'id': user.id, 'name': user.name}


@app.route('/users/<int:user_id>/create_address', methods=['POST'])
def create_address(user_id):
    input_address = request.get_json().get('address')
    data_repository.create_bitcoin_address(user_id=user_id, address_url=input_address)
    return {'message': 'Address created successfully', 'new_address': input_address}


@app.route('/internal/trigger', methods=['POST'])
def trigger_batch():
    sync_wallet_data.syncWalletData()
    return {'status': 'Triggered Sync wallet data job'}


@app.route('/addresses/<int:user_id>', methods=['GET'])
def view_user_address_data(user_id):
    addresses = data_repository.get_all_addresses_for_user(user_id).all()

    addresses_list = []
    for address in addresses:
        address_info = {
            'id': address.id,
            'address_url': address.address_url,
            'user_id': address.user_id,
            'final_balance': address.final_balance,
            'number_of_transactions': address.number_of_transactions,
            'total_received': address.total_received,
            'total_sent': address.total_sent
        }
        addresses_list.append(address_info)
    return {'addresses': addresses_list}


@app.route('/transactions/<string:address_url>', methods=['GET'])
def get_transactions(address_url):
    transactions = data_repository.get_all_transactions_for_address_url(address_url).all()
    transactions_list = []
    for transaction in transactions:
        transaction_info = {
            'id': transaction.id,
            'balance': transaction.balance,
            'total_value': transaction.total_value,
            'fee': transaction.fee,
            'time': transaction.transaction_time
        }
        transactions_list.append(transaction_info)

    return {'transactions': transactions_list}


if __name__ == '__main__':
    app.run(debug=True)
