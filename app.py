import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/apresentacao")
def apresentacao():
  return render_template('apresentacao.html')

@app.route("/contato")
def contato():
  return render_template('contato.html') 

@app.route("/materias")
def materias():
  return render_template('materias.html') 