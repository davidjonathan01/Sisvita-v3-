from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.libreta import Libreta
from schemas.libreta_schema import libreta_schema, libretas_schema

libreta_routes = Blueprint("libreta_routes", __name__)

@libreta_routes.route('/libreta_estado', methods=['POST'])
def create_libreta():
    id_estudiante = request.json.get('id_estudiante')
    per_academico = request.json.get('per_academico')
    nota_promedio = request.json.get('nota_promedio')
    observaciones = request.json.get('observaciones')

    new_libreta = Libreta(id_estudiante=id_estudiante, per_academico=per_academico, nota_promedio=nota_promedio, observaciones=observaciones)

    db.session.add(new_libreta)
    db.session.commit()

    result = libreta_schema.dump(new_libreta)

    data = {
        'message': 'Nueva libreta registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@libreta_routes.route('/get_libretas', methods=['GET'])
def get_libretas():
    all_libretas = Libreta.query.all()
    result = libretas_schema.dump(all_libretas)

    data = {
        'message': 'Todos los registros de libretas han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@libreta_routes.route('/get_libreta/<int:id>', methods=['GET'])
def get_libreta(id):
    libreta = Libreta.query.get(id)

    if not libreta:
        data = {
            'message': 'Libreta no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = libreta_schema.dump(libreta)

    data = {
        'message': 'Libreta encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@libreta_routes.route('/update_libreta/<int:id>', methods=['PUT'])
def update_libreta(id):
    libreta = Libreta.query.get(id)

    if not libreta:
        data = {
            'message': 'Libreta no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    libreta.id_estudiante = request.json.get('id_estudiante')
    libreta.per_academico = request.json.get('per_academico')
    libreta.nota_promedio = request.json.get('nota_promedio')
    libreta.observaciones = request.json.get('observaciones')

    db.session.commit()

    result = libreta_schema.dump(libreta)

    data = {
        'message': 'Libreta actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@libreta_routes.route('/delete_libreta/<int:id>', methods=['DELETE'])
def delete_libreta(id):
    libreta = Libreta.query.get(id)

    if not libreta:
        data = {
            'message': 'Libreta no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(libreta)
    db.session.commit()

    data = {
        'message': 'Libreta eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)