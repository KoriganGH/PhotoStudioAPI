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
# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/orders/', data={'action': 'get_all', 'type': 'company'})
#
# print(resp.text)

# params = {
#     'action': 'update',
#     'type': 'company',
#     'id': '1',
#     'exec': '1',
#     'order_name': 'sssss',
#     'order_creator': '1',
#     'description': 'dawdaw',
#     'deadline': '2023-10-05',
#     'lab': '1',
#     'status': 'da2'
# }
#
# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/orders/', data=params)
#
# print(resp.text)
#
# params = {
#     'action': 'add',
#     'type': 'type1',
#     'editor': '1',
#     'header': 'dawdwd',
#     'content': 'dawdaw',
# }
#
# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/news/', data=params)
#
# print(resp.text)

# params = {
#     'id': '1',
#     'action': 'update',
#     'type': 'type1',
#     'editor': '1',
#     'header': 'XXXXXXXX',
#     'content': 'XXXXXXXXXX',
# }
#
# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/news/', data=params)
#
# print(resp.text)