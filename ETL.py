import requests
import json

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
    id = data["id"]

    # salva o nome do arquivo .json na pasta como o id do usuário .json
    with open(f"{path}/{id}.json", "w") as file:
        json.dump(data, file)


# endpoint_users = "https://dummyjson.com/users/"
# endpoint_products = "https://dummyjson.com/products/"

# # extrai até o final todos os dados presentes na API através de um loop infinito que quebra ao terminar os usuários na API
# count = 1
# while True:
#     data_users = extract_data(endpoint_users + str(count))
#     if data_users:
#         load_data(data_users, "users")
#     else:
#         print(f"Erro na extração dos dados da API: {data_users}")
#         break
#     count += 1

def loop_load_data(endpoint):
    endpoint = 'https://dummyjson.com/' + endpoint

    count = 1
    while True:
        data = extract_data(endpoint + str(count))
        if data:
            load_data(data, endpoint)
        else:
            print(f"Erro na extração dos dados da API: {data}")
            break
        count += 1

endpoints = ["users", "products"]

for endpoint in endpoints:
    loop_load_data(endpoint)
