import requests

requisicao = requests.get("http://httpbin.org/ip")
print(requisicao)
json_to_dict = requisicao.json()
print(json_to_dict)
print(json_to_dict["origin"])