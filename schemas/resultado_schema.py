from utils.ma import ma
from models.resultado import Resultado
from marshmallow import fields
from schemas.especialista_schema import Especialista_Schema
from schemas.evaluacion_schema import Evaluacion_Schema

class Resultado_Schema(ma.Schema):
    class Meta:
        model = Resultado
        fields = ('id_evaluacion',
                  'id_especialista',
                  'puntaje',
                  'interpretacion',
                  'fec_resultado',
                  'especialista',
                  'evaluacion'
                 )
    
    especialista = fields.Nested(Especialista_Schema)
    evaluacion=fields.Nested(Evaluacion_Schema)


resultado_schema = Resultado_Schema()
resultados_schema = Resultado_Schema(many=True)