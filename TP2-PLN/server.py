from flask import Flask, render_template, request
import json
import re
app = Flask(__name__)

file = open("Final.json", "r", encoding="utf-8")

db = json.load(file) 
file.close()

@app.route("/")
def home():
    return render_template("home.html", title="Welcome!!!")


@app.route("/terms")
def terms():
    return render_template("terms.html", designations=db.keys())


@app.route("/term/<t>")
def term(t):
    return render_template("term.html", designation = t, value= db.get(t,"None"))


@app.route("/table")
def table():
    lista = []
    for designation, description in db.items():
        lista.append((designation,description))
    return render_template("table.html", lista=lista)

@app.route("/terms/search")
def search():
    text = request.args.get("text")
    lista = []
    if text:
        for designation, description in db.items():
            if re.search(text,designation,flags=re.I): 
                lista.append((designation,description))
    return render_template("search.html",matched = lista)

@app.route("/term", methods=["POST"])
def addTerm():
    print(request.form)
    designation = request.form["designation"]
    description = request.form["description"]
    english = request.form["english"]
    spanish = request.form["spanish"]

    if designation not in db:
        info_message = "Term Added correctly"
    else:
        info_message = "Term Updated correctly!"

    db[designation] = {"desc":description, "ENG":english, "ES":spanish}
    file_save = open("Final.json", "w", encoding="utf-8")
    json.dump(db,file_save, ensure_ascii=False, indent=4)
    file_save.close()

    return render_template("terms.html", designations=db.keys(), message = info_message)



@app.route("/term/<designation>", methods=["DELETE"])
def deleteTerm(designation):
    desc = db[designation]
    if designation in db:
        print(designation)
        del db[designation]
        print(db.get(designation))
        file_save = open("Final.json","w")
        json.dump(db,file_save, ensure_ascii=False, indent=4)
        file_save.close()
        
    return {designation: {"desc":desc}}

@app.route("/edit/<designation>")
def editTerm(designation):

    return render_template("editTerm.html", designations=db.keys())


app.run(host="localhost", port=3000, debug=True)
