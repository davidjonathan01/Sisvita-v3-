from utils.ma import ma
from models.libreta import Libreta
from marshmallow import fields
from schemas.estudiante_schema import Estudiante_Schema

class Libreta_Schema(ma.Schema):
    class Meta:
        model=Libreta
        fields=('id_libreta',
                'id_estudiante',
                'per_academico',
                'nota_promedio',
                'observaciones',
                'estudiante'
               )
        
    estudiante=ma.Nested(Estudiante_Schema)

libreta_schema = Libreta_Schema()
libretas_schema = Libreta_Schema(many=True)