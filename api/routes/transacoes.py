from flask import Blueprint, request, jsonify
from models.transacao import Transacao
from database import transacoes

transacoes_bp = Blueprint("transacoes", __name__)

@transacoes_bp.route("/transacoes", methods=["GET"])
def listar_transacoes():
    return jsonify([t.to_dict() for t in transacoes])

@transacoes_bp.route("/transacoes", methods=["POST"])
def criar_transacao():
    data = request.json
    novo_id = len(transacoes) + 1
    transacao = Transacao(
        novo_id,
        data["usuario_id"],
        data["valor"],
        data["descricao"]
    )
    transacoes.append(transacao)
    return jsonify(transacao.to_dict()), 201
