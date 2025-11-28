from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = "chave_sitebosch"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dta")
def dta():
    return render_template("dta.html")

@app.route("/conteudo")
def conteudo():
    return render_template("conteudo.html")

@app.route("/jornal")
def jornal():
    return render_template("jornal.html")

@app.route("/curriculo")
def curriculo():
    return render_template("curriculo.html")

@app.route("/conteudosExemplo")
def conteudosExemplo():
    return render_template("conteudosExemplo.html")

@app.route("/visitas")
def visitas():
    return render_template("visitas.html")

@app.route("/curiosidades")
def curiosidades():
    return render_template("curriculo.html")


if __name__ == "__main__":
    app.run(debug=True)