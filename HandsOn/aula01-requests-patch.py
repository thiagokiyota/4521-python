import requests

# Para envio de dados via query string
# headers = {"content-type":"application/json"}
data = {
    "nome": "Joao",
    "sobrenome": "Silva"
}

requisicao = requests.patch(
    "http://httpbin.org/patch",
    # Para envio de dados via query string
    # data=data,
    json=data
    # headers=headers
)
json_to_dict = requisicao.json()

print(json_to_dict)