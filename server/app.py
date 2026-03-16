

from flask import Flask, request, current_app, g, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

customers = ["bob", "bill", "john", "sarah"]

app = Flask(__name__)



@app.route('/contract/<int:id>')
def get_contract(id):
    
    found_contract = None

    for contact in contracts:
        if contact["id"] == id:
            found_contract = contact
            break 

    if found_contract:
        return found_contract["contract_information"], 200
    else:
        return {"error": "Contract not found"}, 404


@app.route('/customer/<customer_name>')
def get_customer(customer_name):

    customer_exists = False

    for name in customers:
        if name == customer_name:
            customer_exists = True
            break

    if customer_exists:
    
        return '', 204
    else:
        return {"error": "Customer not found"}, 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)