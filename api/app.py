from flask import Flask
from routes.users import users_bp
from routes.transacoes import trans_bp
from database import criar_tabelas

app = Flask(__name__)

criar_tabelas()

app.register_blueprint(users_bp)
app.register_blueprint(trans_bp)

if __name__ == "__main__":
    app.run(debug=True)
