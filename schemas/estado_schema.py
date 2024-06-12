from utils.ma import ma
from models.estado import Estado
from marshmallow import fields


class Estado_Schema(ma.Schema):
    class Meta:
        model=Estado
        fields = ('id_estado',
                  'nombre',
                  'descripcion'
                  )


estado_schema = Estado_Schema()
estados_schema = Estado_Schema(many=True)
