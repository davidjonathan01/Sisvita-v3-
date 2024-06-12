import bcrypt

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.especialista import Especialista
from schemas.especialista_schema import especialista_schema, especialistas_schema

especialista_routes = Blueprint("especialista_routes", __name__)

@especialista_routes.route('/create_especialista', methods=['POST'])
def create_especialista():
    id_especialidad = request.json.get('id_especialidad')
    doc_identidad = request.json.get('doc_identidad')
    nombres = request.json.get('nombres')
    apellidos = request.json.get('apellidos')
    fec_nacimiento = request.json.get('fec_nacimiento')
    id_genero = request.json.get('id_genero')
    email = request.json.get('email')
    n_licencia = request.json.get('n_licencia')
    anio_ingreso = request.json.get('anio_ingreso')
    contrasenia = request.json.get('contrasenia')

    contrasenia = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())

    new_especialista = Especialista(id_especialidad=id_especialidad, doc_identidad=doc_identidad, nombres=nombres, apellidos=apellidos, fec_nacimiento=fec_nacimiento, id_genero=id_genero, email=email, n_licencia=n_licencia, anio_ingreso=anio_ingreso, contrasenia=contrasenia)

    db.session.add(new_especialista)
    db.session.commit()

    result = especialista_schema.dump(new_especialista)

    data = {
        'message': 'Nuevo especialista registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@especialista_routes.route('/get_especialistas', methods=['GET'])
def get_especialistas():
    all_especialistas = Especialista.query.all()
    result = especialistas_schema.dump(all_especialistas)

    data = {
        'message': 'Todos los registros de especialistas han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@especialista_routes.route('/get_especialista/<int:id>', methods=['GET'])
def get_especialista(id):
    especialista = Especialista.query.get(id)

    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = especialista_schema.dump(especialista)

    data = {
        'message': 'Especialista encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@especialista_routes.route('/update_especialista/<int:id>', methods=['PUT'])
def update_especialista(id):
    especialista = Especialista.query.get(id)

    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    especialista.id_especialidad = request.json.get('id_especialidad')
    especialista.doc_identidad = request.json.get('doc_identidad')
    especialista.nombres = request.json.get('nombres')
    especialista.apellidos = request.json.get('apellidos')
    especialista.fec_nacimiento = request.json.get('fec_nacimiento')
    especialista.id_genero = request.json.get('id_genero')
    especialista.email = request.json.get('email')
    especialista.n_licencia = request.json.get('n_licencia')
    especialista.anio_ingreso = request.json.get('anio_ingreso')
    contrasenia = request.json.get('contrasenia')
    contrasenia = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())
    especialista.contrasenia = contrasenia

    db.session.commit()

    result = especialista_schema.dump(especialista)

    data = {
        'message': 'Especialista actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@especialista_routes.route('/delete_especialista/<int:id>', methods=['DELETE'])
def delete_especialista(id):
    especialista = Especialista.query.get(id)

    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(especialista)
    db.session.commit()

    data = {
        'message': 'Especialista eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)