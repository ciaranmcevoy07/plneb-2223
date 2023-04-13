from flask import Flask, render_template
import json

app = Flask(__name__)
app.debug = True
file = open("novo_dicionario_medico.json", encoding="utf-8")

db = json.load(file)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/terms")
def egua():
    return render_template('terms.html', designations=db.keys())

@app.route("/term/<t>")
def term(t):
    return render_template('term.html', designations=t, value=db.get(t))

app.run(host="localhost", port=3000, debug=True)

