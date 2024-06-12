from utils.ma import ma
from models.estudiante import Estudiante
from marshmallow import fields
from schemas.genero_schema import Genero_Schema
from schemas.carrera_schema import Carrera_Schema

class Estudiante_Schema(ma.Schema):
    class Meta:
        model=Estudiante
        fields = ('id_estudiante',
              'doc_identidad',
              'nombres',
              'apellidos',
              'fec_nacimiento',
              'id_genero',
              'email',
              'direccion',
              'num_telefono',
              'anio_ingreso',
              'id_carrera',
              'contrasenia',
              'genero',
              'carrera'
              )
    
    genero=ma.Nested(Genero_Schema)
    carrera=ma.Nested(Carrera_Schema)
        
estudiante_schema = Estudiante_Schema()
estudiantes_schema = Estudiante_Schema(many=True)
