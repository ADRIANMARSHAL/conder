from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Crush
from utils import instagram_exists
import os

app = Flask(__name__)
app.secret_key = 'agneswayua'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crushes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit_crush', methods=['GET', 'POST'])
def submit_crush():
    if request.method == 'POST':
        name = request.form.get('crush_name')
        instagram = request.form.get('crush_instagram')

        if not name or not instagram:
            flash("Please fill out both fields.")
            return redirect('/submit_crush')

        instagram = instagram.strip()
        if not instagram.startswith('@'):
            instagram = '@' + instagram

        if not instagram_exists(instagram):
            flash("Instagram account does not exist.")
            return redirect('/submit_crush')

        new_crush = Crush(submitted_by=name, instagram=instagram)
        db.session.add(new_crush)
        db.session.commit()

        flash("Crush submitted successfully!")
        return redirect('/')

    return render_template('index.html')

@app.route('/search')
def search_instagram():
    return render_template('search.html')

@app.route('/results')
def results():
    handle = request.args.get('handle')
    if not handle:
        flash("No handle provided")
        return redirect('/search')
    
    handle = handle.strip()
    if not handle.startswith('@'):
        handle = '@' + handle

    matches = Crush.query.filter(Crush.instagram.ilike(handle)).all()
    return render_template('results.html', handle=handle, matches=matches)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
