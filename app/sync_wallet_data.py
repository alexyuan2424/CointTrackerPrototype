import requests
from app.data_repository import DataRepository

data_repository = DataRepository()


class BitcoinAddressData:
    def __init__(self, address_url, number_of_transactions, total_received, total_sent, final_balance, transactions):
        self.address_url = address_url
        self.number_of_transactions = number_of_transactions
        self.total_received = total_received
        self.total_sent = total_sent
        self.final_balance = final_balance
        self.transactions = transactions


class SyncWalletData:
    def syncWalletData(self):
        allAddresses = data_repository.get_all_addresses()
        for address in allAddresses:
            data = self.getAddressData(address['address_url'])
            self.updateBTCAddressData(data)
            self.saveTransactionData(address['address_url'], data.transactions)

    def getAddressData(self, bitcoin_address):
        # api_url = f"https://blockchain.info/rawaddr/{bitcoin_address}?limit=5"
        api_url = f"https://blockchain.info/rawaddr/{bitcoin_address}"
        response = requests.get(api_url)
        data = response.json()

        address_url = data.get('address')
        number_of_transactions = data.get('n_tx')
        total_received = data.get('total_received')
        total_sent = data.get('total_sent')
        final_balance = data.get('final_balance')
        transactions = data.get('txs', [])
        bitcoin_address_data = BitcoinAddressData(address_url, number_of_transactions,
                                                  total_received, total_sent,
                                                  final_balance, transactions)
        return bitcoin_address_data

    def updateBTCAddressData(self, data):
        data_repository.update_bitcoin_address(data.address_url, data.final_balance,
                                               data.number_of_transactions,
                                               data.total_received, data.total_sent)

    def saveTransactionData(self, bitcoin_address_id, transactions):
        for transaction in transactions:
            data_repository.create_transaction(bitcoin_address_id,
                                               transaction['fee'],
                                               transaction['result'],
                                               transaction['balance'],
                                               transaction['time'])
