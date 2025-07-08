from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)


def conectar():
    return mysql.connector.connect(
        host="db",
        user="usuario",
        password="senha",
        database="loja"
    ) 
@app.route('/')
def index():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    preco = request.form['preco']
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)", (nome, preco))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/deletar/<int:id>')
def deletar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id): 
    conn = conectar()
    cursor = conn.cursor()
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        cursor.execute("UPDATE produtos SET nome = %s, preco = %s WHERE id = %s", (nome, preco, id))
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        cursor.execute("SELECT * FROM produtos WHERE id = %s", (id,))
        produto = cursor.fetchone()
        conn.close()
        return redirect('/')
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)