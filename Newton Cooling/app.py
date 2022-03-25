from flask import Flask, render_template, request
import math

from numpy import float16

app = Flask(__name__)

e = float(2.71828182845)
Ts = int(21)
Tb = int(37)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/sum", methods=["POST", "GET"])
def getvalue():
    Tt = request.form.get("T(t)", type=int) 
    T0 = request.form.get("T0", type=int)
    t = request.form.get("t", type=int)

    k = (math.log((Tt-Ts)/(T0-Ts)))
    k1 = k/t*-1

    x = (math.log((T0-Ts)/(Tb-Ts)))
    x1 = x/k1*-1

    return render_template("sum.html", SUM = x1)

if __name__ == "__main__":
    app.run(debug=True)