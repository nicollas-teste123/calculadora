from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def init():
    print("olaa")
    return render_template("index.html")

@app.route("/env", methods={"POST"})
def log():
    return "logado"


if __name__ == "__main__":
    app.run(debug=True)