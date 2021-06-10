from flask import Flask, render_template, request, redirect, url_for, send_file
from pymongo import MongoClient


#   Creo un instanza del client di mongodb
client = MongoClient("mongodb://localhost:27017/")
#   Creo il db / accedo al db
db = client['VirtualGym']
#   Accedo ad una collezione / creo una collezione
utenti = db['utenti']
app = Flask(__name__)


@app.route('/aboutus', methods=['POST', 'GET'])
def aboutus():
    return render_template("aboutus.html")


@app.route('/calcolo', methods=['POST', 'GET'])
def calcolo():
    return render_template("calcolo_peso.html")


@app.route('/schede', methods=['POST', 'GET'])
def schede():
    return render_template("schede_esercizi.html")


@app.route('/', methods=['POST', 'GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/video', methods=['POST', 'GET'])
def video():
    return render_template("video.html")


@app.route('/orari', methods=['POST', 'GET'])
def orari():
    return render_template("orari.html")


for i in utenti.find():
    print(i)


@app.route('/registrazione', methods=['POST', 'GET'])
def registrazione():
    if request.method == "GET":
        return render_template("registrazione_utente.html")
    else:

        email = request.form["email"]
        password = request.form["psw"]
        acc = {
            "email": email,
            "password": password
        }
        utenti.insert_one(acc)
        return redirect(url_for("homepage"))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form["email"]
        password = request.form["psw"]

        utente = utenti.find_one({"email": email})
        if utente is None:
            print("asgarra")
            return render_template("login.html", succ=0)

        if password == utente["password"]:
            print("ok")
            return render_template("homepage.html", succ=1)

        else:
            print("NO OK")
            return render_template("login.html", succ=0)


if __name__ == '__main__':
    app.run()