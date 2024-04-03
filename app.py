import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def apresentacao():
<!DOCTYPE html>
<html>
    <head>
        <title>Melissa Duarte</title>
    </head>
    <body>
        <h1>Melissa Duarte</h1>
        <h3>Jornalista, 26 anos, Brasília</h3>
        <img src="https://images.jota.info/wp-content/uploads/2023/05/9v9c4401-escolhida-1-682x1024.jpg" 
        alt="Melissa Duarte" width="250" height="350">
        <h3>Sobre mim:</h3>
        <p>Jornalista especializada nas <b>coberturas de saúde e de políticas públicas</b>. Atualmente, é <b>repórter do JOTA</b>.</p> 
        <p>Trabalhou nos jornais <b>O Globo, Poder360 e Correio Braziliense e também atuou nas áreas de cultura, gastronomia, política e educação.</b></p> 
        <p><b>Cursa o Master em Jornalismo de Dados, Automação e Data Storytelling</b> no Insper e <b>se formou em Jornalismo na Universidade de Brasília (UnB)</b>, período em que ganhou o Prêmio Nacional Expocom 2019 na categoria produção de TV.</p>
    </body>
</html>
