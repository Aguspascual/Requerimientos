from flask import Flask, render_template, request, redirect, url_for, Blueprint, session
from models.UsuarioExterno import UsuarioExterno
from utils.db import db
from werkzeug.security import generate_password_hash 

# Define el blueprint
usuarioExterno = Blueprint('usuarioExterno', __name__)

@usuarioExterno.route('/usuario/registrarExterno', methods= ['POST'])
def RegistrarExterno():
    # Obtengo los datos del formulario
    nombre = request.form['nombre']
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']
    correo = request.form['correo']
    tipoUsuario = "Usuario Externo"
    cuil = request.form['cuil']
    descripcion = request.form['descripcion']
    destacado = request.form.get('destacado')
    if destacado:
    # El checkbox está marcado
        destacado = True
    else:
        # El checkbox no está marcado
        destacado = False
    empresa = request.form['empresa']
    #print(destacado)
    # Hashear la contraseña antes de crear el usuario
    hashed_contrasena = generate_password_hash(contrasena)
    # Creo el usuario
    nuevo_usuario = UsuarioExterno(nombre, usuario, hashed_contrasena, correo, tipoUsuario ,cuil, descripcion, destacado, empresa)
    # Lo agrego a la base de datos
    db.session.add(nuevo_usuario)
    db.session.commit()
    return redirect(url_for('usuarios.verUsuarios'))

@usuarioExterno.route('/externo/modificar', methods = ['POST'])
def modInterno():
    # Si no esta iniciada la Sesion, lo redirigo al login
    if session.get('user_active') != True or session.get('user_tipo') != "Interno":
        return redirect(url_for('auth.indexLogin'))
    id = request.form['id']
    externo = UsuarioExterno.query.get(id)
    # Obtengo los datos del formulario
    externo.nombre = request.form['nombre']
    externo.usuario = request.form['usuario']
    contrasena = request.form['contrasena']
    if contrasena != "":
        hashed_contrasena = generate_password_hash(contrasena)
        externo.contrasena = hashed_contrasena
    externo.correo = request.form['correo']
    externo.tipoUsuario = request.form['tipoUsuario']
    externo.cuil = request.form['cuil']
    externo.descripcion = request.form['descripcion']
    externo.empresa = request.form['empresa']
    externo.destacado = request.form['destacado']
    # Confirmo los cambios
    db.session.commit()

    return redirect(url_for('usuarios.verUsuarios'))

@usuarioExterno.route('/externo/eliminar', methods = ['POST'])
def eliminarExterno():
    # Si no esta iniciada la Sesion, lo redirigo al login
    if session.get('user_active') != True or session.get('user_tipo') != "Interno":
        return redirect(url_for('auth.indexLogin'))
    nombre = session.get('user_nombre')
    id = request.form.get('id')
    externo = UsuarioExterno.query.get(id)
    db.session.delete(externo)
    db.session.commit()
    return redirect(url_for('usuarios.verUsuarios')) 