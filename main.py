from flask import Flask, render_template

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['logandreg']
utenti = db['nomediciamotabella']

main = Flask(__name__)


@main.route('/')
def index():
    return render_template('homepage.html')


@main.route('/registrazione_utente.html')
def registrazione():
    return render_template('registrazione_utente.html')


if __name__ == '__main__':
    main.run()
