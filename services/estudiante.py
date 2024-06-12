# insert / update / delete / select / select_all
import bcrypt

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.estudiante import Estudiante
from schemas.estudiante_schema import estudiante_schema, estudiantes_schema

estudiante_routes = Blueprint("estudiante_routes", __name__)

@estudiante_routes.route('/create_estudiante', methods=['POST'])
def create_estudiante():
    doc_identidad = request.json.get('doc_identidad')
    nombres = request.json.get('nombres')
    apellidos = request.json.get('apellidos')
    fec_nacimiento = request.json.get('fec_nacimiento')
    id_genero = request.json.get('id_genero')
    email = request.json.get('email')
    direccion = request.json.get('direccion')
    num_telefono = request.json.get('num_telefono')
    anio_ingreso = request.json.get('anio_ingreso')
    id_carrera = request.json.get('id_carrera')
    contrasenia = request.json.get('contrasenia')

    contrasenia = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())

    new_estudiante = Estudiante(doc_identidad=doc_identidad, nombres=nombres, apellidos=apellidos, fec_nacimiento=fec_nacimiento, id_genero=id_genero, email=email, direccion=direccion, num_telefono=num_telefono, anio_ingreso=anio_ingreso, id_carrera=id_carrera, contrasenia=contrasenia)

    db.session.add(new_estudiante)
    db.session.commit()

    result = estudiante_schema.dump(new_estudiante)

    data = {
        'message': 'Nuevo estudiante registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@estudiante_routes.route('/get_estudiantes', methods=['GET'])
def get_estudiantes():
    all_estudiantes = Estudiante.query.all()
    result = estudiantes_schema.dump(all_estudiantes)

    data = {
        'message': 'Todos los registros de estudiantes han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estudiante_routes.route('/get_estudiante/<int:id>', methods=['GET'])
def get_estudiante(id):
    estudiante = Estudiante.query.get(id)

    if not estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = estudiante_schema.dump(estudiante)

    data = {
        'message': 'Estudiante encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estudiante_routes.route('/update_estudiante/<int:id>', methods=['PUT'])
def update_estudiante(id):
    estudiante = Estudiante.query.get(id)

    if not estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    doc_identificacion = request.json.get('doc_identificacion')
    nombres = request.json.get('nombres')
    apellidos = request.json.get('apellidos')
    fecha_nacimiento = request.json.get('fecha_nacimiento')
    correo_electronico = request.json.get('correo_electronico')
    genero = request.json.get('genero')
    direccion = request.json.get('direccion')
    numero_telefono = request.json.get('numero_telefono')
    carrera_universitaria = request.json.get('carrera_universitaria')
    año_ingreso = request.json.get('año_ingreso')
    contrasenia = request.json.get('contrasenia')

    contrasenia = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())

    estudiante.doc_identificacion = doc_identificacion
    estudiante.nombres = nombres
    estudiante.apellidos = apellidos
    estudiante.fecha_nacimiento = fecha_nacimiento
    estudiante.correo_electronico = correo_electronico
    estudiante.genero = genero
    estudiante.direccion = direccion
    estudiante.numero_telefono = numero_telefono
    estudiante.carrera_universitaria = carrera_universitaria
    estudiante.año_ingreso = año_ingreso
    estudiante.contrasenia = contrasenia

    db.session.commit()

    result = estudiante_schema.dump(estudiante)

    data = {
        'message': 'Estudiante actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estudiante_routes.route('/delete_estudiante/<int:id>', methods=['DELETE'])
def delete_estudiante(id):
    estudiante = Estudiante.query.get(id)

    if not estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(estudiante)
    db.session.commit()

    data = {
        'message': 'Estudiante eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)