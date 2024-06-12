#models/test.py
from utils.db import db
from datetime import datetime

class Test(db.Model):
    __tablename__ = 'test'
    
    id_test = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    n_preguntas = db.Column(db.Integer, nullable=False)
    version = db.Column(db.String(20), nullable=False)
    idioma = db.Column(db.String(20), nullable=False)

    evaluaciones = db.relationship('Evaluacion', backref='test1', cascade='all, delete-orphan')
    preguntas = db.relationship('Pregunta', backref='test2', cascade='all, delete-orphan')
    escalas = db.relationship('Escala', backref='test3', cascade='all, delete-orphan') #sin cascade

    # constructor de la clase
    def __init__(self, nombre, descripcion, n_preguntas, version, idioma):
        self.nombre = nombre
        self.descripcion = descripcion
        self.n_preguntas = n_preguntas
        self.version = version
        self.idioma = idioma