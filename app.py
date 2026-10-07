from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(
    host="localhost",
    user="biblioteca_app",
    password="biblioteca123",
    database="biblioteca"
)

print("Conectado ao banco!")


@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        cursor = conexao.cursor()

        sql = """
        SELECT * FROM funcionarios
        WHERE usuario = %s AND senha = %s
        """

        valores = (usuario, senha)

        cursor.execute(sql, valores)

        funcionario = cursor.fetchone()

        cursor.close()

        if funcionario:
            return render_template("sistema.html")

        else:
            return "Usuário ou senha incorretos."

    return render_template("index.html")

    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        cursor = conexao.cursor()

        sql = """
        SELECT * FROM funcionarios
        WHERE usuario = %s AND senha = %s
        """

        valores = (usuario, senha)

        cursor.execute(sql, valores)

        funcionario = cursor.fetchone()

        cursor.close()

        if funcionario:
            return render_template("sistema.html")

        else: 
            return print("Usuário ou senha incorreto.")


@app.route("/cadastro_usuario", methods=["GET", "POST"])
def cadastro_usuario():

    if request.method == "POST":

        nome = request.form["nome"]
        matricula = request.form["matricula"]
        email = request.form["email"]

        cursor = conexao.cursor()

        sql = """
        INSERT INTO usuarios (nome, matricula, email)
        VALUES (%s, %s, %s)
        """

        valores = (nome, matricula, email)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()

        print("Usuário cadastrado!")

    return render_template("cadastro_usuario.html")


app.run(host="0.0.0.0", port=5000, debug=True)