from sqlalchemy.orm import relationship

from utils.db import db

class Carrera(db.Model):
    __tablename__ = 'carrera'

    id_carrera = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)

    # constructor de la clase
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion