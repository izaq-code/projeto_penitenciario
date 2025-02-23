from flask import Flask

def create_app():
    app = Flask(__name__)  # Criação da instância do Flask
    from app.routes import main  # Importando as rotas definidas no arquivo routes.py
    app.register_blueprint(main)  # Registrando o blueprint com as rotas
    return app  # Retorna a instância do app Flask configurada
