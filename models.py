from . import app, db
from flask_sqlalchemy import SQLAlchemy


class Recette(db.Model):
    id_recette = db.Column(db.Integer, primary_key=True)
    nom_recette = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    nbre_part = db.Column(db.String(100), nullable=True)
    temp_cuiss = db.Column(db.String(100), nullable=True)
    id_chef = db.Column(db.Integer, nullable=False)
    niveau = db.Column(db.String(100), nullable=True)
    categorie = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'{self.id_recette}:{self.nom_recette}:{self.description}:{self.nbre_part}:{self.temp_cuiss}:{self.id_chef}:{self.niveau}:{self.niveau}:{self.categorie}'
