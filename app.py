from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personnel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# MODELE
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Personnel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    prenom = db.Column(db.String(100))
    poste = db.Column(db.String(100))
    date_embauche = db.Column(db.DateTime, default=datetime.utcnow)

# ROUTES
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash("Inscription réussie. Connectez-vous.")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home'))
        flash("Nom d'utilisateur ou mot de passe incorrect")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/personnel')
def personnel():
  
    return render_template('personnel.html', personnel=personnel)

@app.route('/add_personnel', methods=['GET', 'POST'])
def add_personnel():
    
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        poste = request.form['poste']
        date_embauche = datetime.strptime(request.form['date_embauche'], '%Y-%m-%d')
        nouveau = Personnel(nom=nom, prenom=prenom, poste=poste, date_embauche=date_embauche)
        db.session.add(nouveau)
        db.session.commit()
        return redirect(url_for('personnel'))
    return render_template('add_personnel.html')

@app.route('/edit_personnel', methods=['GET', 'POST'])
def edit_personnel():
   
    
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        poste = request.form['poste']
        date_embauche = datetime.strptime(request.form['date_embauche'], '%Y-%m-%d')
        db.session.commit()
        return redirect(url_for('personnel'))
    return render_template('edit_personnel.html')

@app.route('/delete_personnel')
def delete_personnel():
   
   
    db.session.delete()
    db.session.commit()
    return redirect(url_for('personnel'))

if __name__ == '__main__':
    app.run(debug=True)
