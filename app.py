from flask import Flask, render_template, request, jsonify
import requests  # Libreria per chiamate HTTP

app = Flask(__name__)

# URL API del backend dati_bot
API_BASE_URL = "http://127.0.0.1:5001/api"

@app.route('/')
def home():
    """Carica la homepage"""
    return render_template('index.html')

@app.route('/prodotti')
def prodotti():
    """Recupera i prodotti e le categorie dal backend e li invia al template"""
    try:
        categoria = request.args.get('category')
        sconto_minimo = request.args.get('discount', type=int, default=0)

        # Richiesta API con filtri
        params = {}
        if categoria and categoria != "all":
            params['category'] = categoria
        if sconto_minimo > 0:
            params['discount'] = sconto_minimo

        prodotti_response = requests.get(f"{API_BASE_URL}/prodotti", params=params)
        prodotti = prodotti_response.json() if prodotti_response.status_code == 200 else []

        categorie_response = requests.get(f"{API_BASE_URL}/categorie")
        categorie = categorie_response.json() if categorie_response.status_code == 200 else []

    except Exception as e:
        prodotti, categorie = [], []
        print(f"Errore API: {e}")

    return render_template('prodotti.html', prodotti=prodotti, categorie=categorie)

@app.route('/api/categorie')
def categorie():
    """Recupera la lista delle categorie e la restituisce al frontend"""
    try:
        response = requests.get(f"{API_BASE_URL}/categorie")
        categorie = response.json() if response.status_code == 200 else []
    except Exception as e:
        categorie = []
        print(f"Errore API categorie: {e}")

    return jsonify(categorie)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)  # Sito su porta 5002
