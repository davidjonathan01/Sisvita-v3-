from utils.ma import ma
from models.especialista import Especialista
from marshmallow import fields
from schemas.especialidad_schema import Especialidad_Schema
from schemas.genero_schema import Genero_Schema

class Especialista_Schema(ma.Schema):
    class Meta:
        model=Especialista
        fields = ('id_especialista',
                  'id_especialidad',
                  'doc_identidad',
                  'nombres',
                  'apellidos',
                  'fec_nacimiento',
                  'id_genero',
                  'email',
                  'n_licencia',
                  'anio_graduacion',
                  'contrasenia',
                  'especialidad',
                  'genero'
                  )
        
    especialidad=ma.Nested(Especialidad_Schema)
    genero=ma.Nested(Genero_Schema)


especialista_schema = Especialista_Schema()
especialistas_schema = Especialista_Schema(many=True)
