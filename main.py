import json

import requests
from settings import username,password

# базовый URL
base_url = 'https://petstore.swagger.io/v2'

# GET /user/login

res = requests.get(f'{base_url}/user/login?login={username}&password={password}',
                   headers={'accept': 'application/json'})
print('GET /user/login  Logs user into the system')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json())
print('  Ответ сервера header:', res.headers, '\n')

# POST /pet  Добваление питомца
body= {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "kot",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
body=json.dumps(body)
res = requests.post(f'{base_url}/pet', headers={'accept': 'application/json',
                                           'Content-Type': 'application/json'}, data=body)
pet_id=res.json()['id']
print('POST /pet  Add a new pet to the store')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# PUT /pet  Обновление информации о питомце

body= {
  "id": pet_id,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie1",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
body = json.dumps(body)
res = requests.put(f'{base_url}/pet', headers={'accept': 'application/json',
                                               'Content-Type': 'application/json'}, data=body)

print('PUT /pet  Update an existing pet')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# DELETE /pet/{petId} Удаление питомца

res = requests.delete(f'{base_url}/pet/{pet_id}', headers={'accept': 'application/json'})

print('DELETE /pet/{petId}  Deletes a pet')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')