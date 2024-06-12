from sqlalchemy.orm import relationship

from utils.db import db

class Estado(db.Model):
    __tablename__ = 'estado'

    id_estado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    
    tratamientos = relationship('Tratamiento', back_populates='estado', overlaps="estado")

    # constructor de la clase
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
