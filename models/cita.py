from sqlalchemy.orm import relationship
from utils.db import db

class Cita(db.Model):
    __tablename__ = 'cita'

    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), primary_key=True, nullable=False)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), primary_key=True, nullable=False)
    motivo = db.Column(db.String(50), nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey('estado.id_estado'), nullable=False)
    id_modalidad = db.Column(db.Integer, db.ForeignKey('modalidad.id_modalidad'), nullable=False)
    fec_programada = db.Column(db.DateTime, nullable=False)

    estudiante = relationship('Estudiante', backref='citas_estudiante', overlaps="estudiante,citas")
    especialista = relationship('Especialista', backref='citas_especialista', overlaps="especialista,citas")
    estado = relationship('Estado', backref='citas_estado', overlaps="estado,citas")
    modalidad = relationship('Modalidad', backref='citas_modalidad', overlaps="modalidad,citas")

    # constructor de la clase
    def __init__(self, id_estudiante, id_especialista, motivo, id_estado, id_modalidad, fec_programada):
        self.id_estudiante = id_estudiante
        self.id_especialista = id_especialista
        self.motivo = motivo
        self.id_estado = id_estado
        self.id_modalidad = id_modalidad
        self.fec_programada = fec_programada
