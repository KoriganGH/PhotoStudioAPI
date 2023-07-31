import requests

# params = {
#     'action': 'add',
#     'first_name': 'Pavel',
#     'surname': 'Romantsov',
#     'number': '+79064334014',
#     'email': 'kata0880gmail.com',
#     'role': 'Директор',
#     'lab': 'lab1',
#     'permissions': {'status': 1000},
#     'orders_count': '2'
# }
#
# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/user/', data=params)
#
# print(resp)


# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/user/', data={'action': 'delete', 'id': '3'})
#
# print(resp)

# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/user/', data={'action':'update', 'id': '13', 'surname': 'XXXXXX23'})
#
# print(resp)


# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/user/', data={'action':'get_user', 'date': '2023-07-31', 'lab': '1'})
#
# print(resp.text)


# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/schedule/', data={'action': 'add', 'employee': '1', 'date': '2023-10-31', 'lab':'1'})
#
# print(resp)
#
session = requests.Session()
resp = session.post('http://127.0.0.1:8000/orders/', data={'action': 'get_all'})

print(resp.text)
