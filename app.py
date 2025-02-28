from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prodotti')
def prodotti():
    return render_template('prodotti.html')

@app.route('/software')
def software():
    return render_template('software.html')

@app.route('/contatti')
def contatti():
    return render_template('contatti.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
