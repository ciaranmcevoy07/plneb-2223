from flask import Flask, render_template, url_for
import json

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html', title ="Welcome",)






app.run(host="localhost", port=4002, debug=True)
'''@app.route('/api/termos')
def termos_api():
    jsonFile = json.load(dbFile)
    return json.dump(jsonFile) engenharia hegua elefante'''