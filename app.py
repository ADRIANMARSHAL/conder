from flask import Flask, render_template, request, redirect, flash
from utils import instagram_exists
import os
import json

app = Flask(__name__)
app.secret_key = 'agneswayua'  # ✅ this will now work properly

DATA_FILE = os.path.join(os.path.dirname(__file__), 'crushes.json')

def load_crushes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_crushes(crushes):
    with open(DATA_FILE, 'w') as f:
        json.dump(crushes, f, indent=2)

@app.route('/')
def home():
    return render_template('home.html')

def submit_crush():
    if request.method == 'POST':
        name = request.form.get('crush_name', '').strip()
        instagram = request.form.get('crush_instagram', '').strip

        if not name or not instagram:
            flash("Please fill out both fields.")
            return redirect('/submit_crush')

        # Clean up and standardize the Instagram handle
        instagram = instagram.strip()
        if not instagram.startswith('@'):
            instagram = '@' + instagram

        if not instagram_exists(instagram):
            flash("Instagram account does not exist.")
            return redirect('/submit_crush')

        crushes = load_crushes()
        crushes.append({'name': name, 'instagram': instagram})
        save_crushes(crushes)

        flash("Crush submitted successfully!")
        return redirect('/')
    
    return render_template('index.html')
@app.route('/submit_crush', methods=['GET', 'POST'])
def submit_crush():
    if request.method == 'POST':
        name = request.form.get('crush_name')
        instagram = request.form.get('crush_instagram')

        if not name or not instagram:
            flash("Please fill out both fields.")
            return redirect('/submit_crush')

        # Clean up and standardize the Instagram handle
        instagram = instagram.strip()
        if not instagram.startswith('@'):
            instagram = '@' + instagram

        if not instagram_exists(instagram):
            flash("Instagram account does not exist.")
            return redirect('/submit_crush')

        crushes = load_crushes()
        crushes.append({'name': name, 'instagram': instagram})
        save_crushes(crushes)

        flash("Crush submitted successfully!")
        return redirect('/')
    
    return render_template('index.html')


@app.route('/search')
def search_instagram():
    return render_template('search.html')

@app.route('/results')
def results():
    handle = request.args.get('handle')
    crushes = load_crushes()
    matches = [c for c in crushes if c['instagram'].lower() == handle.lower()]
    return render_template('results.html', handle=handle, matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
