from sqlalchemy.orm import relationship

from utils.db import db

class Comentario(db.Model):
    __tablename__ = 'comentario'
    id_comentario=db.Column(db.Integer, primary_key=True,  autoincrement=True)
    id_post = db.Column(db.Integer, db.ForeignKey('post.id_post'), nullable=False)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    fec_publicacion = db.Column(db.Date, nullable=False)
    fec_edicion = db.Column(db.Date, nullable=True)
    anonimo = db.Column(db.Boolean, nullable=False)

    post = relationship('Post', backref='comentario')
    estudiante = relationship('Estudiante', backref='comentario')
    
    # constructor de la clase
    def __init__(self, id_post, id_estudiante, descripcion, fec_publicacion, fec_edicion, anonimo):
        self.id_post = id_post
        self.id_estudiante = id_estudiante
        self.descripcion = descripcion
        self.fec_publicacion = fec_publicacion
        self.fec_edicion = fec_edicion
        self.anonimo = anonimo