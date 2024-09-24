from flask import Flask, render_template, request, redirect, Blueprint
from database import db
from flask_migrate import Migrate
from models import Usuario
from routes.home import home_route

from routes.usuario import usuario_route

app = Flask(__name__)

app.secret_key = 'minha_chave_secreta'

conexao = "sqlite:///meubanco.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(home_route)
app.register_blueprint(usuario_route, url_prefix='/usuarios')

if __name__ == '__main__':
    app.run()