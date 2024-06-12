from utils.ma import ma
from models.test import Test
from marshmallow import fields

class Test_Schema(ma.Schema):
    class Meta:
        model=Test
        fields=('id_test',
               'nombre',
               'descripcion',
               'n_preguntas',
               'version',
               'idioma'
               )

test_schema = Test_Schema()
tests_schema = Test_Schema(many=True)