from sqlalchemy.orm import relationship

from utils.db import db

class Post(db.Model):
    __tablename__ = 'post'

    id_post = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    fec_publicacion = db.Column(db.Date, nullable=False)
    fec_edicion = db.Column(db.Date, nullable=True)
    anonimo = db.Column(db.Boolean, nullable=False)
    n_comentarios = db.Column(db.Integer, nullable=False)

    estudiante = relationship('Estudiante', backref='post')

    comentarios = relationship('Comentario', backref='post1', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, id_estudiante, descripcion, fec_publicacion, fec_edicion, anonimo, n_comentarios):
        self.id_estudiante = id_estudiante
        self.descripcion = descripcion
        self.fec_publicacion = fec_publicacion
        self.fec_edicion = fec_edicion
        self.anonimo = anonimo
        self.n_comentarios = n_comentarios