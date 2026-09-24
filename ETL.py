import requests
import json
import os

# função de extração dos dados da API
def extract_data(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na extração dos dados da API: {response.status_code}")
        return None


# função de carregamento dos dados da API para um arquivo .json em uma pasta, no caso a pasta 'users'
def load_data(data, path):
    # cria a pasta e verifica se ela existe (se existir ele meio que não cria)
    os.makedirs(path, exist_ok=True)
    # salva o nome do arquivo .json na pasta como o id do usuário .json
    with open(f"{path}/{data['id']}.json", "w") as file:
        json.dump(data, file)
        
def loop_load_data(endpoint):
    base_url = f"https://dummyjson.com/{endpoint}"
    count = 1

    while True:
        data = extract_data(f"{base_url}/{count}")
        if data:
            load_data(data, endpoint)
        else:
            print(f"Erro na extração dos dados da API: {data}")
            break
        count += 1


endpoints = ["users", "products"]

for endpoint in endpoints:
    loop_load_data(endpoint)
