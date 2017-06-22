from flask import Flask, jsonify
from coneccion import Invernadero
app = Flask("bd")
inv = Invernadero()

@app.route("/")
def raiz():
    return "Hola"

@app.route("/usuarios")
def usuarios():
    usuarios = inv.mostrar_usuario()
    print(usuarios)
    respuesta = jsonify(usuarios)
    return respuesta #"Usuarios"
           
app.run()