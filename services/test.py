from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.test import Test
from schemas.test_schema import test_schema, tests_schema

test_routes = Blueprint("test_routes", __name__)

@test_routes.route('/create_test', methods=['POST'])
def create_test():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')
    n_preguntas = request.json.get('n_preguntas')
    version = request.json.get('version')
    idioma = request.json.get('idioma')

    new_test = Test(nombre=nombre, descripcion=descripcion, n_preguntas=n_preguntas, version=version, idioma=idioma)

    db.session.add(new_test)
    db.session.commit()

    result = test_schema.dump(new_test)

    data = {
        'message': 'Nuevo test creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@test_routes.route('/get_tests', methods=['GET'])
def get_tests():
    all_tests = Test.query.all()
    result = tests_schema.dump(all_tests)

    data = {
        'message': 'Todos los tests han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@test_routes.route('/get_test/<int:id>', methods=['GET'])
def get_test(id):
    test = Test.query.get(id)
    result = test_schema.dump(test)

    data = {
        'message': 'Test encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@test_routes.route('/update_test/<int:id>', methods=['PUT'])
def update_test(id):
    test = Test.query.get(id)

    test.nombre = request.json.get('nombre')
    test.descripcion = request.json.get('descripcion')
    test.n_preguntas = request.json.get('n_preguntas')
    test.version = request.json.get('version')
    test.idioma = request.json.get('idioma')

    db.session.commit()

    result = test_schema.dump(test)

    data = {
        'message': 'Test actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@test_routes.route('/delete_test/<int:id>', methods=['DELETE'])
def delete_test(id):
    test = Test.query.get(id)

    db.session.delete(test)
    db.session.commit()

    data = {
        'message': 'Test eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)