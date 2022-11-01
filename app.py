from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#database
cred = credentials.Certificate('/home/belini/Documents/prog/webproject/virtualenv/blacktie-2a2a9-firebase-adminsdk-59nbn-f6c28ab314.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()


#classe para o formulario de cadasto
class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

#app flask
app = Flask(__name__)

@app.route('/inicio')
def home():
    return render_template('index.html', titulo='Home')
    
@app.route('/login')
def login():
    return render_template('cadastro.html', titulo_login='Cadastro')

@app.route('/criar')
def criar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    usuario = Usuario(nome, email, senha)


app.run()
