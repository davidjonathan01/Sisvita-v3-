# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.evaluacion import Evaluacion
from schemas.evaluacion_schema import evaluacion_schema, evaluaciones_schema

evaluacion_routes = Blueprint("evaluacion_routes", __name__)

@evaluacion_routes.route('/create_evaluacion', methods=['POST'])
def create_evaluacion():
    id_estudiante = request.json.get('id_estudiante')
    id_test = request.json.get('id_test')
    respuestas_formulario = request.json.get('respuestas_formulario')
    fec_realizacion = request.json.get('fec_realizacion')

    new_evaluacion = Evaluacion(id_estudiante=id_estudiante, id_test=id_test, respuestas_formulario=respuestas_formulario, fec_realizacion=fec_realizacion)

    db.session.add(new_evaluacion)
    db.session.commit()

    result = evaluacion_schema.dump(new_evaluacion)

    data = {
        'message': 'Nuevo registro de evaluación creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@evaluacion_routes.route('/get_evaluaciones', methods=['GET'])
def get_evaluaciones():
    all_evaluaciones = Evaluacion.query.all()
    result = evaluaciones_schema.dump(all_evaluaciones)

    data = {
        'message': 'Todos los registros de evaluaciones han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@evaluacion_routes.route('/get_evaluacion/<int:id>', methods=['GET'])
def get_evaluacion(id):
    evaluacion = Evaluacion.query.get(id)

    if not evaluacion:
        data = {
            'message': 'Evaluación no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = evaluacion_schema.dump(evaluacion)

    data = {
        'message': 'Evaluación encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@evaluacion_routes.route('/update_evaluacion/<int:id>', methods=['PUT'])
def update_evaluacion(id):
    evaluacion = Evaluacion.query.get(id)

    if not evaluacion:
        data = {
            'message': 'Evaluación no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_estudiante = request.json.get('id_estudiante')
    id_test = request.json.get('id_test')
    respuestas_formulario = request.json.get('respuestas_formulario')
    fec_realizacion = request.json.get('fec_realizacion')

    evaluacion.id_estudiante = id_estudiante
    evaluacion.id_test = id_test
    evaluacion.respuestas_formulario = respuestas_formulario
    evaluacion.fec_realizacion = fec_realizacion

    db.session.commit()

    result = evaluacion_schema.dump(evaluacion)

    data = {
        'message': 'Evaluación actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@evaluacion_routes.route('/delete_evaluacion/<int:id>', methods=['DELETE'])
def delete_evaluacion(id):
    evaluacion = Evaluacion.query.get(id)

    if not evaluacion:
        data = {
            'message': 'Evaluación no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(evaluacion)
    db.session.commit()

    data = {
        'message': 'Evaluación eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)