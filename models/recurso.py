from sqlalchemy.orm import relationship

from utils.db import db

class Recurso(db.Model):
    __tablename__ = 'recurso'

    id_recurso = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(1000), nullable=False)
    palabras_clave = db.Column(db.String(250), nullable=False)
    fec_publicacion = db.Column(db.Date, nullable=False)
    fec_edicion = db.Column(db.Date, nullable=True)

    especialista = relationship('Especialista', backref='recurso')

    # constructor de la clase
    def __init__(self, id_especialista, titulo, descripcion, palabras_clave, fec_publicacion, fec_edicion):
        self.id_especialista = id_especialista
        self.titulo = titulo
        self.descripcion = descripcion
        self.palabras_clave = palabras_clave
        self.fec_publicacion = fec_publicacion
        self.fec_edicion = fec_edicion