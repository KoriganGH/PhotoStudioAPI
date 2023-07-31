import requests

# params = {
#     'first_name': 'Pavel',
#     'surname': 'Romantsov',
#     'number': '+79064334014',
#     'email': 'kata0880gmail.com',
#     'role': 'Директор',
#     'lab': 'lab1',
#     'permissions': {'status': 1000},
#     'orders_count': '2'
# }

# headers = {}
# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/add_new_user/', data=params)

# print(resp)


# headers = {}
# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/delete_user/', data={'id': '6'})
#
# print(resp)

# headers = {}
# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/update_user/', data={'id': '5', 'surname': 'XXXXXX'})

# print(resp)


headers = {}
session = requests.Session()
resp = session.post('http://127.0.0.1:8000/get_user/', data={'lab':'1'})

print(resp.text)


# headers = {}
# session = requests.Session()
# resp = session.post('http://127.0.0.1:8000/schedule_update/', data={'employee_id': '1', 'lab': 'lab1', 'date': '2023-09-03'})

# print(resp.url)
