from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Nom d’utilisateur', validators=[InputRequired()])
    password = PasswordField('Mot de passe', validators=[InputRequired()])
    submit = SubmitField('Connexion')

class RegisterForm(FlaskForm):
    username = StringField('Nom d’utilisateur', validators=[InputRequired()])
    password = PasswordField('Mot de passe', validators=[InputRequired()])
    submit = SubmitField('Créer un compte')
# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cle-secrete-par-defaut'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///personnel.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
