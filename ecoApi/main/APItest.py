import requests
import json
"""Script feito pra testes na API.
Status: Get(V)
        Post(V)
        Put(V)
        Delete(V)
        Imagens()"""


def postCreateUserForne():

    url = 'http://3.86.37.62:8000/api/fornecedores/'

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
    
   
    url = 'http://3.86.37.62:8000/api/compradores/'

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

    url = 'http://3.86.37.62:8000/api/fornecedores/5/'#sempre é bom verificar o ID

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

    url = 'http://3.86.37.62:8000/api/compradores/4/'#sempre é bom verificar o ID

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
    url = 'http://3.86.37.62:8000/api/'+entidade+'/'+id+'/'
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.delete(url,headers=headers)
    print("id > "+id+" deletado")



def getProductList():
    id = '1'
    entidade = 'produto'
    url = 'http://3.86.37.62:8081/api/'+entidade+'/'+id+'/'
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url,headers=headers,)
    if response.status_code == 200:
        try:
            # Parse the JSON content
            json_data = response.json()
            print('JSON Response:', json_data)
        except ValueError:
            print('Falha ao carregar arquivo Json')
    else:
        print('Deu merda ao coletar os dados ->', response.status_code)
    
def getProtectedJWt():
    your_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxMTY0NzcxLCJpYXQiOjE3MjExNjM4NzEsImp0aSI6ImY3OGE4MWVhMWJjNzRhZjE5YWI3ZTYyMjA3YzJhMWQ0IiwidXNlcl9pZCI6MX0.ux4FhdMUaDEH_i8z1ktabXaE8PAVMg8KRoYjvc-sR6k'
    url = 'http://3.86.37.62:8081/api/protected'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {your_token}'
    }
    response = requests.get(url,headers=headers,)
    if response.status_code == 200:
        try:
            # Parse the JSON content
            json_data = response.json()
            print('JSON Response:', json_data)
        except ValueError:
            print('Falha ao carregar arquivo Json')
    else:
        print('Deu merda ao coletar os dados ->', response.status_code)
    
    
getProtectedJWt()