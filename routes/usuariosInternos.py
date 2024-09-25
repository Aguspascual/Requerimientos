from flask import Flask, redirect, Blueprint, request, url_for, session
from models.UsuarioInterno import UsuarioInterno
from utils.db import db
from werkzeug.security import generate_password_hash

# Define el blueprint
usuariosInternos = Blueprint('usuariosInternos', __name__)

@usuariosInternos.route('/usuario/registrarInterno', methods= ['POST'])
def RegistrarInterno():
    # Si no esta iniciada la Sesion, lo redirigo al login
    if session.get('user_active') != True or session.get('user_tipo') != "Interno":
        return redirect(url_for('auth.indexLogin'))
    # Obtengo los datos del formulario
    legajo = request.form['legajo']
    nombre = request.form['nombre']
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']
    correo = request.form['correo']
    cargo = request.form['cargo']
    departamento = request.form['departamento']
    tipoUsuario = "Usuario Interno"
    # Hasheo la contraseña 
    hashed_contrasena = generate_password_hash(contrasena)
    # Creo el usuario
    nuevo_usuario = UsuarioInterno(legajo, nombre, usuario, hashed_contrasena, correo, tipoUsuario, cargo ,departamento)
    # Lo agrego a la base de datos
    db.session.add(nuevo_usuario)
    db.session.commit()
    return redirect(url_for('usuarios.verUsuarios'))

@usuariosInternos.route('/interno/modificar', methods = ['POST'])
def modInterno():
    # Si no esta iniciada la Sesion, lo redirigo al login
    if session.get('user_active') != True or session.get('user_tipo') != "Interno":
        return redirect(url_for('auth.indexLogin'))
    id = request.form['id']
    interno = UsuarioInterno.query.get(id)
    # Obtengo los datos del formulario
    interno.legajo = request.form['legajo']
    interno.nombre = request.form['nombre']
    interno.usuario = request.form['usuario']
    contrasena = request.form['contrasena']
    if contrasena != "":
        hashed_contrasena = generate_password_hash(contrasena)
        interno.contrasena = hashed_contrasena
    interno.correo = request.form['correo']
    interno.cargo = request.form['cargo']
    interno.departamento = request.form['departamento']
    # Confirmo los cambios
    db.session.commit()

    return redirect(url_for('usuarios.verUsuarios'))

@usuariosInternos.route('/interno/eliminar', methods = ['POST'])
def eliminarInterno():
    # Si no esta iniciada la Sesion, lo redirigo al login
    if session.get('user_active') != True or session.get('user_tipo') != "Interno":
        return redirect(url_for('auth.indexLogin'))
    id = request.form.get('id')
    interno = UsuarioInterno.query.get(id)
    db.session.delete(interno)
    db.session.commit()
    return redirect(url_for('usuarios.verUsuarios')) 