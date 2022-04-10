from flask import Flask, render_template, request
import math

app = Flask(__name__)

Tb = int(37)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def result():
    Tt = request.form.get("Tt", type=int)
    T0 = request.form.get("T0", type=int)
    Ts = request.form.get("Ts", type=int)
    t = request.form.get("t", type=int)

    k = (math.log((Tt-Ts)/(T0-Ts)))
    k1 = k/t*-1

    x = (math.log((T0-Ts)/(Tb-Ts)))
    x1 = x/k1*-1

    RES = x1

    return render_template("result.html", RES = RES)