from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.tratamiento import Tratamiento
from schemas.tratamiento_schema import tratamiento_schema, tratamientos_schema

tratamiento_routes = Blueprint("tratamiento_routes", __name__)

@tratamiento_routes.route('/create_tratamiento', methods=['POST'])
def create_tratamiento():
    id_resultado1 = request.json.get('id_resultado1')
    id_resultado2 = request.json.get('id_resultado2')
    id_especialista = request.json.get('id_especialista')
    objetivo = request.json.get('objetivo')
    indicaciones = request.json.get('indicaciones')
    fec_asignacion = request.json.get('fec_asignacion')
    fec_inicio = request.json.get('fec_inicio')
    fec_fin = request.json.get('fec_fin')
    id_estado = request.json.get('id_estado')

    new_tratamiento = Tratamiento(id_resultado1=id_resultado1, id_resultado2=id_resultado2, id_especialista=id_especialista, objetivo=objetivo, indicaciones=indicaciones, fec_asignacion=fec_asignacion, fec_inicio=fec_inicio, fec_fin=fec_fin, id_estado=id_estado)

    db.session.add(new_tratamiento)
    db.session.commit()

    result = tratamiento_schema.dump(new_tratamiento)

    data = {
        'message': 'Nuevo tratamiento registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@tratamiento_routes.route('/get_tratamientos', methods=['GET'])
def get_tratamientos():
    all_tratamientos = Tratamiento.query.all()
    result = tratamientos_schema.dump(all_tratamientos)

    data = {
        'message': 'Todos los registros de tratamientos han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tratamiento_routes.route('/get_tratamiento/<int:id1>/<int:id2>/<int:id3>', methods=['GET'])
def get_tratamiento(id1, id2, id3):
    tratamiento = Tratamiento.query.get(id1, id2, id3)

    if not tratamiento:
        data = {
            'message': 'Tratamiento no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = tratamiento_schema.dump(tratamiento)

    data = {
        'message': 'Tratamiento encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tratamiento_routes.route('/update_tratamiento/<int:id1>/<int:id2>/<int:id3>', methods=['PUT'])
def update_tratamiento(id1, id2, id3):
    tratamiento = Tratamiento.query.get(id1, id2, id3)

    if not tratamiento:
        data = {
            'message': 'Tratamiento no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_resultado1 = request.json.get('id_resultado1')
    id_resultado2 = request.json.get('id_resultado2')
    id_especialista = request.json.get('id_especialista')
    objetivo = request.json.get('objetivo')
    indicaciones = request.json.get('indicaciones')
    fec_asignacion = request.json.get('fec_asignacion')
    fec_inicio = request.json.get('fec_inicio')
    fec_fin = request.json.get('fec_fin')
    id_estado = request.json.get('id_estado')

    tratamiento.id_resultado1 = id_resultado1
    tratamiento.id_resultado2 = id_resultado2
    tratamiento.id_especialista = id_especialista
    tratamiento.objetivo = objetivo
    tratamiento.indicaciones = indicaciones
    tratamiento.fec_asignacion = fec_asignacion
    tratamiento.fec_inicio = fec_inicio
    tratamiento.fec_fin = fec_fin
    tratamiento.id_estado = id_estado

    db.session.commit()

    result = tratamiento_schema.dump(tratamiento)

    data = {
        'message': 'Tratamiento actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tratamiento_routes.route('/delete_tratamiento/<int:id1>/<int:id2>/<int:id3>', methods=['DELETE'])
def delete_tratamiento(id1, id2, id3):
    tratamiento = Tratamiento.query.get(id1, id2, id3)

    if not tratamiento:
        data = {
            'message': 'Tratamiento no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(tratamiento)
    db.session.commit()

    data = {
        'message': 'Tratamiento eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)