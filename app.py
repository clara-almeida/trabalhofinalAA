import os
import requests
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__) # Cria uma instância do Flask. 


@app.route("/")
def apresentacao():
  return render_template('apresentacao.html')

@app.route("/contato")
def contato():
  return render_template('contato.html') 

@app.route("/materias")
def materias():
  return render_template('materias.html') 

@app.route("/discursos")
def discursos():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
         <title> Highlights Discursos do Presidente</title>
    </head>
    <body>
      <h1> Confira os principais trechos dos últimos discursos presidenciais</h1>
      <p> 
        Veja, abaixo, as últimas declarações:
        <ul>
    """
    