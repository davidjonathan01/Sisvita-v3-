from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.recurso import Recurso
from schemas.recurso_schema import recurso_schema, recursos_schema 

recurso_routes = Blueprint("recurso_routes", __name__)

@recurso_routes.route('/create_recurso', methods=['POST'])
def create_recurso():
    id_especialista = request.json.get('id_especialista')
    titulo = request.json.get('titulo')
    descripcion = request.json.get('descripcion')
    palabras_clave = request.json.get('palabras_clave')
    fec_publicacion = request.json.get('fec_publicacion')
    fec_edicion = request.json.get('fec_edicion')

    new_recurso = Recurso(id_especialista=id_especialista, titulo=titulo, descripcion=descripcion, palabras_clave=palabras_clave, fec_publicacion=fec_publicacion, fec_edicion=fec_edicion)

    db.session.add(new_recurso)
    db.session.commit()

    result = recurso_schema.dump(new_recurso)

    data = {
        'message': 'Nuevo recurso registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@recurso_routes.route('/get_recursos', methods=['GET'])
def get_recursos():
    all_recursos = Recurso.query.all()
    result = recursos_schema.dump(all_recursos)

    data = {
        'message': 'Todos los registros de recursos han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@recurso_routes.route('/get_recurso/<int:id>', methods=['GET'])
def get_recurso(id):
    recurso = Recurso.query.get(id)
    result = recurso_schema.dump(recurso)

    data = {
        'message': 'Recurso encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@recurso_routes.route('/update_recurso/<int:id>', methods=['PUT'])
def update_recurso(id):
    recurso = Recurso.query.get(id)

    id_especialista = request.json.get('id_especialista')
    titulo = request.json.get('titulo')
    descripcion = request.json.get('descripcion')
    palabras_clave = request.json.get('palabras_clave')
    fec_publicacion = request.json.get('fec_publicacion')
    fec_edicion = request.json.get('fec_edicion')

    recurso.id_especialista = id_especialista
    recurso.titulo = titulo
    recurso.descripcion = descripcion
    recurso.palabras_clave = palabras_clave
    recurso.fec_publicacion = fec_publicacion
    recurso.fec_edicion = fec_edicion

    db.session.commit()

    result = recurso_schema.dump(recurso)

    data = {
        'message': 'Recurso actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@recurso_routes.route('/delete_recurso/<int:id>', methods=['DELETE'])
def delete_recurso(id):
    recurso = Recurso.query.get(id)
    db.session.delete(recurso)
    db.session.commit()

    data = {
        'message': 'Recurso eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)