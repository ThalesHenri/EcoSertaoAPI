import requests
import json
"""Script feito pra testes na API.
Status: Get(V)
        Post(V)
        Put(V)
        Delete()"""


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

def putUserForne():

    url = 'http://127.0.0.1:8000/api/fornecedores/5/'#sempre é bom verificar o ID

    data = {
        #nome cnpj email telefone
        'nome': 'Pablo Borçal',
        'cnpj': '21938311',
        'email': 'ricardo@hotmail.com',
        'telefone': '83129318123'
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.put(url, data=json.dumps(data), headers=headers)
    print(json.dumps(data))

    print('Status Code:', response.status_code)
    print('Response JSON:', response.json())

def putUserCompr():

    url = 'http://127.0.0.1:8000/api/compradores/4/'#sempre é bom verificar o ID

    data = {
        #nome cnpj email telefone
        'nome': 'Dennis Marcal Pangolao',
        'cpf': '21938311',
        'email': 'ricardo@hotmail.com',
        'telefone': '83129318123'
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.put(url, data=json.dumps(data), headers=headers)
    print(json.dumps(data))

    print('Status Code:', response.status_code)
    print('Response JSON:', response.json())


def deleteTest():
    id = '3'
    entidade = 'fornecedores'
    url = 'http://127.0.0.1:8000/api/'+entidade+'/'+id+'/'
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.delete(url,headers=headers)
    print("id > "+id+" deletado")
deleteTest()
