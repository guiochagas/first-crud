from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    titulo = "Gestão de usuários"
    usuarios = [
        {"nome": "Guilherme", "membro_ativo": True},
        {"nome": "Sarah", "membro_ativo": True},
        {"nome": "Alana", "membro_ativo": False},
        {"nome": "Liam", "membro_ativo": False},

    ]
    return render_template("index.html", titulo=titulo, usuarios=usuarios)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)