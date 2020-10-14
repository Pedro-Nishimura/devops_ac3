import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def cem_primo():

    count = 1
    c = 1

    c =1
    count = 1

    primos = '2, '
    numero = 3
    while count < 100:
        isprimo = 1
        for x in range(2, numero):

            if numero % x == 0:

            if (numero % x == 0):

                isprimo = 0
                break
        if (isprimo):
            primos = primos + str(numero) + ","

            count += 1    
            if count % 10 == 0:
                primos = primos + "<br>"

            count += 1
        if count % 10 == 0:
            primos = primos + "<br>"

        numero += 1
    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
