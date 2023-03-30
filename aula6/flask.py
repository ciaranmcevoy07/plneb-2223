from flask import Flask
import json

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

app.run(host="localhost", port=4002, debug=True)

@app.route('/api/termos')
def termos_api():
    jsonFile = json.load(dbFile)
    return json.dump(jsonFile)