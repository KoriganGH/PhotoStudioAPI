import requests

params = {
    'first_name': 'Pavel',
    'surname': 'Romantsov',
    'number': '+79064334014',
    'role': 'Директор',
    'email': 'kata0880gmail.com',
    'lab': 4,
    'permissions': {'status': 1000},
}

headers = {}
session = requests.Session()
resp = session.post('http://127.0.0.1:8000/test/', data=params)

print(resp)