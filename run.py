#!/usr/bin/python

from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nome = "Fernanda"
    posts = ["Flask Basico","Flask Intermediario","Flask Avancado"]
    return render_template("index.html",nome=nome,posts=posts)

if __name__ == '__main__':
    app.run(debug=True)