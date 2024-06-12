from utils.ma import ma
from models.taller import Taller
from marshmallow import fields
from schemas.especialista_schema import Especialista_Schema

class Taller_Schema(ma.Schema):
    class Meta:
        model = Taller
        fields = ('id_taller',
                  'id_especialista',
                  'n_vacantes',
                  'fec_inicio',
                  'fec_fin',
                  'especialista'
                 )
    
    especialista = fields.Nested(Especialista_Schema)


taller_schema = Taller_Schema()
talleres_schema = Taller_Schema(many=True)