from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def init():
    print("olaa")
    return render_template("index.html")

@app.route("/env", methods={"POST"})
def log():
    if SENHA == request.form.get("senha"):
        return "logado"
    else: 
        return "não logado"



if __name__ == "__main__":
    app.run(debug=True)