from utils.ma import ma
from models.post import Post
from marshmallow import fields
from schemas.estudiante_schema import Estudiante_Schema

class Post_Schema(ma.Schema):
    class Meta:
        model=Post
        fields=('id_post',
                'id_estudiante',
                'descripcion',
                'fec_publicacion',
                'fec_edicion',
                'anonimo',
                'n_comentarios',
                'estudiante'
               )
    
    estudiante = fields.Nested(Estudiante_Schema)

post_schema = Post_Schema()
posts_schema = Post_Schema(many=True)