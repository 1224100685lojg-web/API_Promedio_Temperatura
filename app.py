from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():

    datos = request.get_json()

    valor = datos.get('valor')
    escala = datos.get('escala')

    if valor is None or escala is None:
        return jsonify({"error": "Faltan datos"}), 400

    if escala == "C":
        resultado = (valor * 9/5) + 32
        return jsonify({
            "original": f"{valor}°C",
            "convertido": f"{resultado}°F"
        })

    elif escala == "F":
        resultado = (valor - 32) * 5/9
        return jsonify({
            "original": f"{valor}°F",
            "convertido": f"{resultado}°C"
        })

    else:
        return jsonify({"error": "Escala no válida (usa C o F)"}), 400


if __name__ == '__main__':
    app.run(debug=True)