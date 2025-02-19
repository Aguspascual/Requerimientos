from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from routes.usuarios import usuarios
from routes.usuariosInternos import usuariosInternos
from routes.usuariosExternos import usuarioExterno
from routes.requerimientos import requerimiento, categoriaRequerimiento, tipoRequerimiento, evento, comentario, archivo
from routes.auth import auth
from config import Config
import smtplib
from email.mime.text import MIMEText
import pymysql

app = Flask(__name__)
pymysql.install_as_MySQLdb()

# Cargar la configuración desde config.py
app.config.from_object(Config)

# Inicio la base de datos
db.init_app(app)


# Llamo a la ruta de cada clase
app.register_blueprint(usuarios)
app.register_blueprint(usuariosInternos)  
app.register_blueprint(usuarioExterno)
app.register_blueprint(requerimiento)
app.register_blueprint(categoriaRequerimiento)
app.register_blueprint(tipoRequerimiento)
app.register_blueprint(evento)
app.register_blueprint(comentario)
app.register_blueprint(archivo)
app.register_blueprint(auth)

@app.route('/')
def index():
    return render_template('/auth/auth.html')
    

# Todo lo que se ejecute cuando inicio app.py en forma secuencial
if __name__ == "__main__":
    # Crear todas las tablas que tengo en la base de datos
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=5000, debug=False)