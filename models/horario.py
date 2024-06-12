from sqlalchemy.orm import relationship

from utils.db import db

class Horario(db.Model):
    __tablename__ = 'horario'

    id_horario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_taller = db.Column(db.Integer, db.ForeignKey('taller.id_taller'), nullable=False)
    dia = db.Column(db.Integer, nullable=False)
    horario_inicio = db.Column(db.Time, nullable=False)
    horario_fin = db.Column(db.Time, nullable=False)

    taller = relationship('Taller', backref='horario')
    
    # constructor de la clase
    def __init__(self, id_taller, dia, horario_inicio, horario_fin):
        self.id_taller = id_taller
        self.dia = dia
        self.horario_inicio = horario_inicio
        self.horario_fin = horario_fin