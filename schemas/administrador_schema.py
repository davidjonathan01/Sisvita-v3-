from utils.ma import ma
from models.administrador import Administrador
from marshmallow import fields

class Administrador_Schema(ma.Schema):
    class Meta:
        model=Administrador
        fields = ('id_administrador',
                'nombres',
                'apellidos',
                'email',
                'num_telefono',
                'contrasenia'
                )
        
administrador_schema = Administrador_Schema()
administradores_schema = Administrador_Schema(many=True)
