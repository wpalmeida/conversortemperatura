from flask import Flask, render_template, request

app = Flask(__name__)

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    unidade_origem = None
    unidade_destino = None

    if request.method == 'POST':
        escolha = request.form['escolha']
        temperatura = float(request.form['temperatura'])

        if escolha == 'celsius_para_fahrenheit':
            resultado = celsius_para_fahrenheit(temperatura)
            unidade_origem = 'Celsius'
            unidade_destino = 'Fahrenheit'
        elif escolha == 'fahrenheit_para_celsius':
            resultado = fahrenheit_para_celsius(temperatura)
            unidade_origem = 'Fahrenheit'
            unidade_destino = 'Celsius'

    return render_template('index.html', resultado=resultado, unidade_origem=unidade_origem, unidade_destino=unidade_destino)

if __name__ == '__main__':
    app.run(debug=True)
