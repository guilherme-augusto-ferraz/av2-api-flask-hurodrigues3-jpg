from flask import Flask
from routes.users import users_bp
from routes.transacoes import transacoes_bp

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(transacoes_bp)

@app.route("/")
def home():
    return {"mensagem": "API simples em Flask funcionando!"}

if __name__ == "__main__":
    app.run(debug=True)
