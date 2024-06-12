#models/taller.py
from sqlalchemy.orm import relationship

from utils.db import db

class Taller(db.Model):
    __tablename__ = 'taller'

    id_taller = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), nullable=False)
    n_vacantes = db.Column(db.Integer, nullable=False)
    fec_inicio = db.Column(db.DateTime, nullable=False)
    fec_fin = db.Column(db.DateTime, nullable=False)

    especialista = relationship('Especialista', backref='taller')

    asistencias = relationship('Asistencia', backref='taller2', cascade='all, delete-orphan')
    horarios = db.relationship('Horario', backref='taller3', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, id_especialista, n_vacantes, fec_inicio, fec_fin):
        self.id_especialista = id_especialista
        self.n_vacantes = n_vacantes
        self.fec_inicio = fec_inicio
        self.fec_fin = fec_fin