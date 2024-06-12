from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.resultado import Resultado
from schemas.resultado_schema import resultado_schema, resultados_schema

resultado_routes = Blueprint("resultado_routes", __name__)

@resultado_routes.route('/create_resultado', methods=['POST'])
def create_resultado():
    id_especialista = request.json.get('id_especialista')
    puntaje = request.json.get('puntaje')
    interpretacion = request.json.get('interpretacion')
    fec_resultado = request.json.get('fec_resultado')

    new_resultado = Resultado(id_especialista=id_especialista, puntaje=puntaje, interpretacion=interpretacion, fec_resultado=fec_resultado)

    db.session.add(new_resultado)
    db.session.commit()

    result = resultado_schema.dump(new_resultado)

    data = {
        'message': 'Nuevo resultado registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@resultado_routes.route('/get_resultados', methods=['GET'])
def get_resultados():
    all_resultados = Resultado.query.all()
    result = resultados_schema.dump(all_resultados)

    data = {
        'message': 'Todos los registros de resultados han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@resultado_routes.route('/get_resultado/<int:id1>/<int:id2>', methods=['GET'])
def get_resultado(id1, id2):
    resultado = Resultado.query.get(id1, id2)

    if not resultado:
        data = {
            'message': 'Resultado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = resultado_schema.dump(resultado)

    data = {
        'message': 'Resultado encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@resultado_routes.route('/update_resultado/<int:id1>/<int:id2>', methods=['PUT'])
def update_resultado(id1, id2):
    resultado = Resultado.query.get(id1, id2)

    if not resultado:
        data = {
            'message': 'Resultado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    resultado.id_especialista = request.json.get('id_especialista')
    resultado.puntaje = request.json.get('puntaje')
    resultado.interpretacion = request.json.get('interpretacion')
    resultado.fec_resultado = request.json.get('fec_resultado')

    db.session.commit()

    result = resultado_schema.dump(resultado)

    data = {
        'message': 'Resultado actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@resultado_routes.route('/delete_resultado/<int:id1>/<int:id2>', methods=['DELETE'])
def delete_resultado(id1, id2):
    resultado = Resultado.query.get(id1, id2)

    if not resultado:
        data = {
            'message': 'Resultado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(resultado)
    db.session.commit()

    data = {
        'message': 'Resultado eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)