import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def cem_primo():
    count = 0
    primos = '2, '
    numero = 3
    while count < 99:
        isprimo = True
        for x in range(2, numero):
            if numero % x == 0:
                isprimo = False
                break
        if isprimo is True:
            primos += str(numero) + ","
            count += 1
        numero += 1
        if count % 10 == 0:
            primos += "<br>"
    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
