# CointTrackerPrototype
Setup
Design
API

Overview
This API provides endpoints to manage users, addresses, and transactions in our coin tracker prototype wallet.

1. Create a New User
Path: /users
Method: POST
Description: Create a new user with the provided name.
Request Body:
Format: JSON
Example: {"name": "John Doe"}
Response:
Status: 200 OK
Content: {"message": "User created successfully", "user_id": <user_id>}

2. Get User Details
Path: /users/{user_id}
Method: GET
Description: Retrieve details for a user by their ID.
Parameters:
{user_id}: User ID (integer)
Response:
Status: 200 OK
Content: {"id": <user_id>, "name": "<user_name>"}

3. Create Address for a User
Path: /users/{user_id}/create_address
Method: POST
Description: Create a new address for a user.
Parameters:
{user_id}: User ID (integer)
Request Body:
Format: JSON
Example: {"address": "<address_url>"}
Response:
Status: 200 OK
Content: {"message": "Address created successfully", "new_address": "<address_url>"}

4. Trigger Batch for Syncing Wallet Data
Path: /internal/trigger
Method: POST
Description: Trigger a batch job to sync wallet data.
Response:
Status: 200 OK
Content: {"status": "Triggered Sync wallet data job"}
5. View All Addresses for a User
Path: /addresses/{user_id}
Method: GET
Description: Retrieve all addresses for a user.
Parameters:
{user_id}: User ID (integer)
Response:
Status: 200 OK
Content: {"addresses": [{"id": <address_id>, "address_url": "<address_url>", "user_id": <user_id>, "final_balance": <balance>, "number_of_transactions": <num_transactions>, "total_received": <total_received>, "total_sent": <total_sent>}, ...]}

6. Get All Transactions for an Address
Path: /transactions/{address_url}
Method: GET
Description: Retrieve all transactions for a given address.
Parameters:
{address_url}: Address URL (string)
Response:
Status: 200 OK
Content: {"transactions": [{"id": <transaction_id>, "balance": <balance>, "total_value": <total_value>, "fee": <fee>, "time": "<transaction_time>"}, ...]}
