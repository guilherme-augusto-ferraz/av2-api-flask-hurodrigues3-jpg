class Transacao:
    def __init__(self, id, usuario_id, valor, descricao):
        self.id = id
        self.usuario_id = usuario_id
        self.valor = valor
        self.descricao = descricao

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "valor": self.valor,
            "descricao": self.descricao
        }
