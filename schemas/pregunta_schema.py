from utils.ma import ma
from models.pregunta import Pregunta
from marshmallow import fields

class Pregunta_Schema(ma.Schema):
    class Meta:
        model=Pregunta
        fields=('id_pregunta',
                'id_test',
                'interrogante',
                'descripcion',
                'test'
               )
    
    test = fields.Nested('Test_Schema')

pregunta_schema = Pregunta_Schema()
preguntas_schema = Pregunta_Schema(many=True)