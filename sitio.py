from flask import Flask, render_template, request

app = Flask(__name__)

def contar_vocales(texto):
    vocales = 0
    for i in texto.lower():
        if i in "aeiou":
            vocales += 1
    return vocales

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texto = request.form['texto']
        vocales = contar_vocales(texto)
        return render_template('index.html', vocales=vocales)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
