from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    idade = request.form['idade']
    atividade = request.form['atividade']

    with open('cadastros.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, idade, atividade])
    
    return redirect('/lista')

@app.route('/lista')
def lista():
    cadastros = []
    try:
        with open('cadastros.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    cadastros.append(row)
    except FileNotFoundError:
        cadastros = []

    return render_template('lista.html', cadastros=cadastros)

if __name__ == '__main__':
    app.run(debug=True)
