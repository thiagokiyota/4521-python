from flask import Blueprint, Response, request
from config import mongo_db
from bson.json_util import dumps

users_routes = Blueprint(
    "users",
    __name__,
    url_prefix="/users"
)

@users_routes.route("")
def getUsers():
    try:
        users = mongo_db.user.find()
        return Response(dumps(users), status=200, content_type="application/json")
    except Exception as e:
        return "Erro: %s" %(e)

@users_routes.route("", methods=["POST"])
def postUsers():
    try:
        user = request.get_json()
        mongo_db.user.insert_one(
            {
                "name": user["name"],
                "email": user["email"],
                "messages": []
            }
        )
        response = {
            "message": "Usuário '%s' criado com sucesso!" %(user["name"])
        }
        return Response(dumps(response), status=201, content_type="application/json")
    except Exception as e:
        return "Erro %s" %(e)

@users_routes.route("", methods=["PATCH"])
def patchUsers():
    try:
        user = request.get_json()
        updated = mongo_db.user.update_one(
            { "email": user["email"] },
            { "$set": user }
        )
        if updated.modified_count:
            response = { "message": "Usuário '%s' atualizado com sucesso!"%(user["name"]) }
            return Response(dumps(response), status=200, content_type="application/json")
        elif updated.matched_count:
            response = { "message": "Usuário '%s' encontrado, mas não foi modificado."%(user["name"]) }
            return Response(dumps(response), status=400, content_type="application/json")
        else:
            response = { "message": "Usuário '%s' não foi encontrado!"%(user["name"]) }
            return Response(dumps(response), status=404, content_type="application/json")
    except Exception as e:
        return "Erro: %s" %(e)

@users_routes.route("", methods=["DELETE"])
def deleteUsers():
    try:
        user = request.get_json()
        deleted = mongo_db.user.delete_one(
            { "email": user["email"] },
        )
        if deleted.deleted_count:
            response = { "message": "Usuário '%s' removido com sucesso!"%(user["email"]) }
            return Response(dumps(response), status=200, content_type="application/json")
        else:
            response = { "message": "Usuário '%s' não foi encontrado!"%(user["email"]) }
            return Response(dumps(response), status=404, content_type="application/json")
    except Exception as e:
        return "Erro: %s" %(e)