from sqlalchemy.orm import relationship

from utils.db import db

class Administrador(db.Model):
    __tablename__ = 'administrador'

    id_administrador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombres = db.Column(db.String(150), nullable=False)
    apellidos = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    num_telefono = db.Column(db.Numeric(9), nullable=False)
    contrasenia = db.Column(db.String(255), nullable=False)
    
    # constructor de la clase
    def __init__(self, nombres, apellidos, email, num_telefono, contrasenia):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.num_telefono = num_telefono
        self.contrasenia = contrasenia