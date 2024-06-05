import requests
import json

def postCreateUserForne():

    url = 'http://127.0.0.1:8000/api/fornecedores/'

    data = {
        #nome cnpj email telefone
        'nome': 'Pablo Marcal',
        'cnpj': '21938311',
        'email': 'ricardo@hotmail.com',
        'telefone': '83129318123'
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(json.dumps(data))

    print('Status Code:', response.status_code)
    print('Response JSON:', response.json())


def postCreateUserCompr():
    
   
    url = 'http://127.0.0.1:8000/api/compradores/'

    data = {
        #nome cnpj email telefone
        'nome': 'Dennis Marcal',
        'cpf': '21938311',
        'email': 'ricardo@hotmail.com',
        'telefone': '83129318123'
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(json.dumps(data))

    print('Status Code:', response.status_code)
    print('Response JSON:', response.json())

postCreateUserCompr()
