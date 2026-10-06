# Conectar python + HTML + MySQL
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA_SENHA",
    database="biblioteca"
)

@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":

        nome = request.form["nome"]
        matricula = request.form["matricula"]
        email = request.form["email"]

        print(nome)
        print(matricula)
        print(email)

    return render_template("index.html")

app.run(debug=True)

