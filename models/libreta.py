from sqlalchemy.orm import relationship

from utils.db import db

class Libreta(db.Model):
    __tablename__ = 'libreta'

    id_libreta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), nullable=False)
    per_academico = db.Column(db.String(20), nullable=False)
    nota_promedio = db.Column(db.Float, nullable=False)
    observaciones = db.Column(db.String(250), nullable=False)

    estudiante = relationship('Estudiante', backref='libreta')
    
    # constructor de la clase
    def __init__(self, id_estudiante, per_academico, nota_promedio, observaciones):
        self.id_estudiante = id_estudiante
        self.per_academico = per_academico
        self.nota_promedio = nota_promedio
        self.observaciones = observaciones