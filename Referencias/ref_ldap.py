#!/usr/bin/env python3

from ldap3 import Server, Connection, MODIFY_REPLACE
from hashlib import md5
from binascii import b2a_base64

username= "admin"
password= "4linux"

server= Server("ldap://192.168.0.200:389")
ldap_con= Connection(
    server,
    "cn=%s,dc=dexter,dc=com,dc=br"%(username),
    password
)
ldap_con.bind()

#### Criar um objeto ####
# md5json = md5("senhapadrao".encode("utf-8")).digest()
# user = {
#     "cn": "joao",
#     "sn": "hummel",
#     "mail": "joao.hummel@4linux.com.br",
#     "uidNumber": "123",
#     "gidNumber": "123",
#     "uid": "joao.hummel@4linux.com.br",
#     "homeDirectory": "/home/joao",
#     "userPassword": "{md5}" + b2a_base64(md5json).decode("utf-8")
# }
# objectClass = ["top", "person", "inetOrgPerson", "posixAccount", "organizationalPerson"]
# dn = "uid=%s,dc=dexter,dc=com,dc=br"%(user["mail"])
# user_added = ldap_con.add(dn, objectClass, user)

#### Pesquisar um objeto ####
# email = "joao.hummel@4linux.com.br"
# dn = "uid=%s,dc=dexter,dc=com,dc=br"%(email)
# ldap_con.search(
#     dn,
#     "(objectclass=person)",
#     attributes=["sn", "userPassword"]
# )
# print(ldap_con.entries)

#### Atualizar um objeto ####
# email = "joao.hummel@4linux.com.br"
# dn = "uid=%s,dc=dexter,dc=com,dc=br"%(email)
# change = {
#     "gn": [MODIFY_REPLACE, ["João"]],
#     "cn": [MODIFY_REPLACE, ["João Gabriel"]]
# }
# ldap_con.modify(
#     dn,
#     change
# )
# print(ldap_con.result)

#### Remover um objeto ####
# email = "joao.hummel@4linux.com.br"
# dn = "uid=%s,dc=dexter,dc=com,dc=br"%(email)
# print(ldap_con.delete(dn))






