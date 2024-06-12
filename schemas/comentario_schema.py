from utils.ma import ma
from models.comentario import Comentario
from marshmallow import fields
from schemas.post_schema import Post_Schema
from schemas.estudiante_schema import Estudiante_Schema

class Comentario_Schema(ma.Schema):
    class Meta:
        model=Comentario
        fields = ('id_post',
                  'id_estudiante',
                  'descripcion',
                  'fec_publicacion',
                  'fec_edicion',
                  'anonimo',
                  'post',
                  'estudiante'
                  )
        
    post=ma.Nested(Post_Schema)
    estudiante=ma.Nested(Estudiante_Schema)
        
comentario_schema = Comentario_Schema()
comentarios_schema = Comentario_Schema(many=True)
