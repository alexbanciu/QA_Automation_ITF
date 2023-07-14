import requests
from requests_folder.get_token import generate_token


def delete_order(order_id):
    token = generate_token()
    print(token)
    header_params = {'Authorization': token}
    r = requests.delete(f"https://simple-books-api.glitch.me/orders/{order_id}", headers=header_params)
    return r
