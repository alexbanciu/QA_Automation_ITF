import random
import requests

def generate_token():
    nr = random.randint(1, 99999999999999999999999999999)
    request_body = {
        "clientName": "Postman_TA30",
        "clientEmail": f"ta{nr}@example.com"
    }
    r = requests.post('https://simple-books-api.glitch.me/api-clients/', json=request_body)
    token = r.json()["accessToken"]
    # r.json() este rezultatul request-ului si este in format json cu o structura interioara de tip dictionar
    # r.json()["accessToken"] accesam valoarea cheii accessToken
    return token
