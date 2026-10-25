from flask import Flask, jsonify, abort
import pymysql
import requests

app = Flask(__name__)

def get_connection():
    return pymysql.connect(
        host="db",
        user="clase",
        password="clase123",
        database="creditos",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.errorhandler(404)
def manejar_404(error):
    return {
        "error": {
            "code": 404,
            "message": error.description or "Recurso no encontrado"
        }
    }, 404

@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando"
    }

@app.get("/clientes")
def obtener_clientes():
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes_credito LIMIT 100")
            clientes = cursor.fetchall()
    finally:
        conexion.close()

    return jsonify(clientes)


@app.get("/clientes/<id>")
def obtener_cliente(id):
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM clientes_credito WHERE ID=%s",
                (id,)
            )
            cliente = cursor.fetchone()
    finally:
        conexion.close()

    if cliente is None:
        abort(404, description="Cliente no encontrado")

    return jsonify(cliente)

@app.get("/clientes/estado-civil/<estado>")
def clientes_estado_civil(estado):
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM clientes_credito WHERE Estado_Civil=%s",
                (estado,)
            )
            clientes = cursor.fetchall()
    finally:
        conexion.close()

    return jsonify(clientes)

@app.get("/clientes/proposito/<proposito>")
def clientes_proposito(proposito):
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM clientes_credito WHERE Proposito=%s",
                (proposito,)
            )
            clientes = cursor.fetchall()
    finally:
        conexion.close()

    return jsonify(clientes)

@app.get("/clientes/estudios/<estudios>")
def clientes_por_estudios(estudios):
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM clientes_credito WHERE Estudios=%s",
                (estudios,)
            )
            clientes = cursor.fetchall()
    finally:
        conexion.close()

    return jsonify(clientes)

@app.get("/clientes/jornada/<jornada>")
def clientes_por_jornada(jornada):
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM clientes_credito WHERE Tipo_Jornada_Laboral=%s",
                (jornada,)
            )
            clientes = cursor.fetchall()
    finally:
        conexion.close()

    return jsonify(clientes)



@app.get("/edad-aleatoria")
def edad_aleatoria():
    nombre = request.args.get("name", "pablo")
    
    respuesta = requests.get(
        f"https://api.agify.io/?name={nombre}"
    )

    return respuesta.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)