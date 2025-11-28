from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)