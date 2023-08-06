import requests

params = {
    'username': 'xxxxxx34',
    'first_name': 'xxxx',
    'last_name': 'xxxx',
    'number': '+79024334014',
    'email': 'kata@gmail.com',
    'role': 'role1',
    'lab': '1',
    'permissions': 'dwadwa',
    'orders_count': '2',
    'telegram_id': '1',
    'password': '123'
}

session = requests.Session()
resp = session.post('http://127.0.0.1:8000/user/create/', data=params)

print(resp.text)

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


# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/user/', data={'action': 'get_all'})
#
# print(resp.text)


# resp = requests.get('http://127.0.0.1:8000/TEST/', headers={'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwOTExMDk1LCJpYXQiOjE2OTA5MTA3OTUsImp0aSI6IjQ4N2MxOTZiNTlhMjRkMzlhZTQyYjQ3ZmRlNGUzZjFkIiwidXNlcl9pZCI6MX0.yH_pD4pA_klQSCp_Z1oJqHbfcuNLltfovxh_dcy_FUI'})
#
# print(resp.text)
