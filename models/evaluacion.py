#models/evaluacion.py
from sqlalchemy.orm import relationship
from utils.db import db

class Evaluacion(db.Model):
    __tablename__ = 'evaluacion'

    id_evaluacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), nullable=False)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'), nullable=False)
    respuestas = db.Column(db.String(300), nullable=False)
    fec_realizacion = db.Column(db.Date, nullable=False)

    estudiante = db.relationship('Estudiante', back_populates='evaluaciones')
    test = db.relationship('Test', back_populates='evaluaciones')

    resultados = db.relationship('Resultado', backref='evaluacion1', cascade='all, delete-orphan')

    # constructor de la clase
    def __init__(self, id_estudiante, id_test, respuestas, fec_realizacion):
        self.id_estudiante = id_estudiante
        self.id_test = id_test
        self.respuestas = respuestas
        self.fec_realizacion = fec_realizacion
