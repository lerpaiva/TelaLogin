from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=[ "GET","POST"])
def login():
    conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="cadastros"
)
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM cad WHERE email = %s AND senha = %s", (email, senha))

        resultados = cursor.fetchall()

        if resultados:
            cursor.close()
            conexao.close()
            return redirect(url_for('home')) 
        else:
            cursor.close()
            conexao.close()
            return render_template('forms.html', logado=False)
    return render_template("forms.html", logado=False)

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
