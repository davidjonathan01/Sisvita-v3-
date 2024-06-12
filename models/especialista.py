from sqlalchemy.orm import relationship

from utils.db import db

class Especialista(db.Model):
    __tablename__ = 'especialista'

    id_especialista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_especialidad = db.Column(db.Integer, db.ForeignKey('especialidad.id_especialidad'), nullable=False)
    doc_identidad = db.Column(db.String(20), nullable=False)
    nombres = db.Column(db.String(150), nullable=False)
    apellidos = db.Column(db.String(200), nullable=False)
    fec_nacimiento = db.Column(db.Date, nullable=False)
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id_genero'), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    n_licencia = db.Column(db.String(11), nullable=False)
    anio_graduacion = db.Column(db.Integer, nullable=False)
    contrasenia = db.Column(db.String(255), nullable=False)

    especialidad = relationship('Especialidad', backref='especialista1')
    genero = relationship('Genero', backref='especialista2')

    citas = relationship('Cita', backref='especialista3', cascade='all, delete-orphan')
    resultados = relationship('Resultado', backref='especialista4', cascade='all, delete-orphan')
    talleres = relationship('Taller', backref='especialista5', cascade='all, delete-orphan')
    recursos = relationship('Recurso', backref='especialista6', cascade='all, delete-orphan')
    tratamientos = relationship('Tratamiento', backref='especialista7', cascade='all, delete-orphan')

    # constructor de la clase
    def __init__(self, id_especialidad, doc_identidad, nombres, apellidos, fec_nacimiento, id_genero, email, n_licencia, anio_graduacion):
        self.id_especialidad = id_especialidad
        self.doc_identidad = doc_identidad
        self.nombres = nombres
        self.apellidos = apellidos
        self.fec_nacimiento = fec_nacimiento
        self.id_genero = id_genero
        self.email = email
        self.n_licencia = n_licencia
        self.anio_graduacion = anio_graduacion