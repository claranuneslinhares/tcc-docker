from flask import Flask, request, render_template, redirect
import mysql.connector
from os import environ

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
   