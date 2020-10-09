#!/usr/bin/env python3

from pymongo import MongoClient

mongo_con = MongoClient()
db = mongo_con["flask-app"]

# inserted = db.user.insert_one(
#     {
#         "name": "edu",
#         "email": "edu@gmail.com",
#         "messeges": [
#             {
#                 "name": "edu",
#                 "message": "mensagem"
#             }
#         ]
#     }
# )
# print(inserted)


# user = db.user.find_one(
#     {
#         "name": "edu",
#         "email": "edu@gmail.com.br"
#     }
# )
# print(user)
# print(user["_id"].generation_time)

# user = db.user.update_one(
#     {
#         "name": "edu",
#         "email": "edu@gmail.com.br"
#     },
#     {
#         "$set": {
#             "email": "edu@gmail.com"
#         }
#     }
# )
# print(user.matched_count, user.modified_count)


# deleted = db.user.delete_one(
#     {
#         "name": "edu",
#     }
# )
# print(deleted.deleted_count)


# updated = db.user.update_one(
#     {
#         "name": "edu",
#     },
#     {
#         "$push": {
#             "messages": {
#                 "name": "edu",
#                 "message": "message",
#                 "age": 5
#             }
#         }
#     }
# )
# print(updated.matched_count, updated.modified_count)


# updated = db.user.update_one(
#     {
#         "name": "edu",
#     },
#     {
#         "$push": {
#             "messages": {
#                 "age": 3
#             }
#         }
#     }
# )
# print(updated.matched_count, updated.modified_count)


# updated = db.user.update_one(
#     {
#         "name": "edu",
#     },
#     {
#         "$set": {
#             "messages.message": "teste"
#         }
#     }
# )
# print(updated.matched_count, updated.modified_count)