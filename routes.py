from . import app, models
from flask import render_template, request, redirect, url_for


@app.route('/')
@app.route('/accueil')
def catalogue_de_recette():
    liste_categories = models.Recette.query.distinct('categorie')
    return render_template('tous_recettes.html', title='Bienvenu dans notre site des recettes', liste=type(liste_categories), liste_cat=liste_categories)


@app.route('/tous_recettes')
def montrer_recettes():
    nom_cat = request.args.get('nom_categorie')
    liste_recettes = models.Recette.query.filter_by(categorie=nom_cat)
    return render_template('detail_recette.html', title='Detail de la recette', recettes=liste_recettes,
                           typerecettes=type(liste_recettes), cat=nom_cat)
