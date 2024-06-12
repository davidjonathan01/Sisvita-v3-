from sqlalchemy.orm import relationship

from utils.db import db

class Pregunta(db.Model):
    __tablename__ = 'pregunta'

    id_pregunta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'), nullable=False)
    interrogante = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)

    test = relationship('Test', backref='pregunta')
    
    # constructor de la clase
    def __init__(self, id_test, interrogante, descripcion):
        self.id_test = id_test
        self.interrogante = interrogante
        self.descripcion = descripcion