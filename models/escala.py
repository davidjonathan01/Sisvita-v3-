from sqlalchemy.orm import relationship

from utils.db import db

class Escala(db.Model):
    __tablename__ = 'escala'

    id_escala = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'), nullable=False)

    test = relationship('Test', backref='escala')
    
    # constructor de la clase
    def __init__(self, nombre, descripcion, id_test):
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_test = id_test