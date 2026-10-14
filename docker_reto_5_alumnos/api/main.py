from flask import Flask, jsonify, request, abort
import pymysql
from data_loader import cargar_excel

app = Flask(__name__)

clientes = cargar_excel()


def get_connection():
    return pymysql.connect(
        host="db",
        user="clase",
        password="clase123",
        database="creditos",
        cursorclass=pymysql.cursors.DictCursor
    )



@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando"
    }


@app.get("/clientes/<id>")
def obtener_cliente(id):
    cliente = next((c for c in clientes if c["ID"] == id), None)
    if cliente is None:
        abort(404, description="Cliente no encontrado")
    return jsonify(cliente)


@app.get("/clientes")
def obtener_clientes():
    conexion = get_connection()

    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM clientes_credito LIMIT 100")
        clientes = cursor.fetchall()

    conexion.close()

    return jsonify(clientes)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)