from flask import Blueprint, request, jsonify
from database import get_connection

trans_bp = Blueprint("transacoes", __name__)

@trans_bp.route("/transacoes", methods=["GET"])
def listar_transacoes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transacoes;")
    dados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(dados)

@trans_bp.route("/transacoes", methods=["POST"])
def criar_transacao():
    dados = request.get_json()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transacoes (usuario_id, valor, tipo)
        VALUES (?, ?, ?)
    """, (dados["usuario_id"], dados["valor"], dados["tipo"]))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Transação criada"}), 201

@trans_bp.route("/transacoes/<int:id>", methods=["PUT"])
def atualizar_transacao(id):
    dados = request.get_json()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transacoes SET valor=?, tipo=?
        WHERE id=?
    """, (dados["valor"], dados["tipo"], id))

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"erro": "Transação não encontrada"}), 404

    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Transação atualizada"})

# ------ NOVO: DELETE ------
@trans_bp.route("/transacoes/<int:id>", methods=["DELETE"])
def excluir_transacao(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transacoes WHERE id=?", (id,))

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"erro": "Transação não encontrada"}), 404

    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Transação excluída"})
