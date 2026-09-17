import requests
# import json

def extract_data(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na extração dos dados da API: {response.status_code}")
        return None

endpoint_users = 'https://dummyjson.com/users/1'
endpoint_products = 'https://dummyjson.com/products/1'

data_users = extract_data(endpoint_users)

print(data_users)