#models/estudiante.py
from sqlalchemy.orm import relationship
from utils.db import db

class Estudiante(db.Model):
    __tablename__ = 'estudiante'

    id_estudiante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doc_identidad = db.Column(db.String(20), nullable=False, unique=True)
    nombres = db.Column(db.String(150), nullable=False)
    apellidos = db.Column(db.String(200), nullable=False)
    fec_nacimiento = db.Column(db.Date, nullable=False)
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id_genero'), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    num_telefono = db.Column(db.Numeric(9), nullable=False)
    anio_ingreso = db.Column(db.Integer, nullable=False)
    id_carrera = db.Column(db.Integer, db.ForeignKey('carrera.id_carrera'), nullable=False)
    contrasenia = db.Column(db.String(255), nullable=False)

    genero = relationship('Genero', backref='estudiantes')
    carrera = relationship('Carrera', backref='estudiantes')

    citas = relationship('Cita', backref='estudiante_citas', cascade='all, delete-orphan', overlaps="estudiante,citas_estudiante")
    libretas = relationship('Libreta', backref='estudiante_libretas', cascade='all, delete-orphan', overlaps="estudiante,libreta")
    posts = relationship('Post', backref='estudiante_posts', cascade='all, delete-orphan', overlaps="estudiante,post")
    comentarios = relationship('Comentario', backref='estudiante_comentarios', cascade='all, delete-orphan', overlaps="estudiante,comentario")
    evaluaciones = relationship('Evaluacion', back_populates='estudiante', cascade='all, delete-orphan', overlaps="estudiante,evaluacion")
    asistencias = relationship('Asistencia', backref='estudiante_asistencias', cascade='all, delete-orphan', overlaps="estudiante,asistencia")

    # constructor de la clase
    def __init__(self, doc_identidad, nombres, apellidos, fec_nacimiento, id_genero, email, direccion, num_telefono, anio_ingreso, id_carrera,contrasenia):
        self.doc_identidad = doc_identidad
        self.nombres = nombres
        self.apellidos = apellidos
        self.fec_nacimiento = fec_nacimiento
        self.id_genero = id_genero
        self.email = email
        self.direccion = direccion
        self.num_telefono = num_telefono
        self.anio_ingreso = anio_ingreso
        self.id_carrera = id_carrera
        self.contrasenia=contrasenia
