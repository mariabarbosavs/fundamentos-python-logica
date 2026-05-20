import requests

resposta_get = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(f"Codigo de status: {resposta_get.status_code}")
print(f"Dados so Usuário: {resposta_get.json()}")