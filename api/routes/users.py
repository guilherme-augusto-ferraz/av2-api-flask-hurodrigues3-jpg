from flask import Blueprint, request, jsonify
from database import get_connection

users_bp = Blueprint("usuarios", __name__)

@users_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios;")
    dados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(dados)

@users_bp.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.get_json()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", 
                   (dados["nome"], dados["email"]))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Usuário criado"}), 201

@users_bp.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id=?", (id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify(dict(row))
    return jsonify({"erro": "Usuário não encontrado"}), 404
