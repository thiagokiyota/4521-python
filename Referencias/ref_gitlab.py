#!/usr/bin/env python3

import requests
import json

# token de acesso
token = "QT95C2zL6vBssWwsni6t"

#### Listagem dos Projetos ####
# projetos = requests.get("http://192.168.0.100/api/v4/projects?private_token=%s"%(token))
# print(
#     json.dumps(
#         projetos.json(),
#         indent=4,
#         sort_keys=True
#     )
# )

#### Criação de Projeto ####
# data = {
#     "name": "flask-app"
# }
# projeto = requests.post("http://192.168.0.100/api/v4/projects?private_token=%s"%(token), data)
# print(projeto.json())

#### Listagem dos Usuários ####
# usuarios = requests.get("http://192.168.0.100/api/v4/users?private_token=%s"%(token))
# print(
#     json.dumps(
#         usuarios.json(),
#         indent=4,
#         sort_keys=True
#     )
# )

#### Criação de Usuário ####
# data = {
#     "email": "nick@4linux.com.br",
#     "username": "nick",
#     "name": "Nick",
#     "password": "4linux123"
# }
# usuario = requests.post("http://192.168.0.100/api/v4/users?private_token=%s"%(token), data)
# print(usuario.json())

# project_id = 2
# data = {
#     "user_id": 2,
#     "access_level": 40
# }
# projeto = requests.post("http://192.168.0.100/api/v4/projects/%s/members?private_token=%s"%(project_id, token), data)
# print(projeto.json())







