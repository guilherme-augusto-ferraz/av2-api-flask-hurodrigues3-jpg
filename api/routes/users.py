from flask import Blueprint, request, jsonify
from models.user import Usuario
from database import usuarios

users_bp = Blueprint("users", __name__)

@users_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify([u.to_dict() for u in usuarios])

@users_bp.route("/usuarios", methods=["POST"])
def criar_usuario():
    data = request.json
    novo_id = len(usuarios) + 1
    usuario = Usuario(novo_id, data["nome"], data["email"])
    usuarios.append(usuario)
    return jsonify(usuario.to_dict()), 201

@users_bp.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    for u in usuarios:
        if u.id == id:
            return jsonify(u.to_dict())
    return jsonify({"erro": "Usuário não encontrado"}), 404
