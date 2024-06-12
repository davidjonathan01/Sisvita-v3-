from sqlalchemy.orm import relationship

from utils.db import db

class Asistencia(db.Model):
    __tablename__ = 'asistencia'

    id_asistencia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.Date, nullable=False)
    id_taller = db.Column(db.Integer, db.ForeignKey('taller.id_taller'), nullable=False)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), nullable=False)

    taller = relationship('Taller', backref='asistencia')
    estudiante = relationship('Estudiante', backref='asistencia')
    
    # constructor de la clase
    def __init__(self, fecha, id_taller, id_estudiante):
        self.fecha = fecha
        self.id_taller = id_taller
        self.id_estudiante = id_estudiante