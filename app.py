from flask import Flask, jsonify, render_template
import socket
from pokeneas import get_random_pokenea

app = Flask(__name__)

# Ruta para devolver información en formato JSON
@app.route('/api/pokenea')
def get_pokenea():
    pokenea = get_random_pokenea()
    response = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": socket.gethostname()
    }
    return jsonify(response)

# Ruta para mostrar la imagen y la frase filosófica
@app.route('/pokenea')
def show_pokenea():
    pokenea = get_random_pokenea()
    return render_template('pokenea.html', pokenea=pokenea, contenedor_id=socket.gethostname())

# Ruta para el home
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
