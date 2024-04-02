import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Olá, <b>tudo bem</b>?"

@app.route("/teste")
def teste():
  return "Essa página é um <b>teste</b>" 

@app.route("/telegram", methods=["POST"])
def telegram_update():
    update = request.json
    url_envio_mensagem = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    chat_id = update ["message"]["chat"]["id"]
    mensagem = {"chat_id": chat_id, "text": "mensagem <b> recebida</b>!", "parse_mode": "HTML"}
    requests.post(url_envio_mensagem, data=mensagem)
    return "ok"