from flask import Flask, jsonify, abort, request
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

@app.errorhandler(400)
def manejar_400(error):
    return {
        "error": {
            "code": 400,
            "message": error.description or "Datos de entrada incorrectos"
        }
    }, 400

@app.errorhandler(404)
def manejar_404(error):
    return {
        "error": {
            "code": 404,
            "message": error.description or "El recurso no existe"
        }
    }, 404

@app.errorhandler(405)
def manejar_405(error):
    return {
        "error": {
            "code": 405,
            "message": "Metodo no permitido"
        }
    }, 405

@app.errorhandler(409)
def manejar_409(error):
    return {
        "error": {
            "code": 409,
            "message": error.description or "Conflicto con el estado actual"
        }
    }, 409

@app.errorhandler(415)
def manejar_415(error):
    return {
        "error": {
            "code": 415,
            "message": "Formato recibido no soportado"
        }
    }, 415

@app.errorhandler(500)
def manejar_500(error):
    return {
        "error": {
            "code": 500,
            "message": "Error inesperado en el servidor"
        }
    }, 500

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

@app.get("/clientes/buscar")
def buscar_clientes():
    cliente_id = request.args.get("id")
    estudios = request.args.get("estudios")
    
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            if cliente_id:
                cursor.execute("SELECT * FROM clientes_credito WHERE ID LIKE %s LIMIT 100", (f"%{cliente_id}%",))
            elif estudios:
                cursor.execute("SELECT * FROM clientes_credito WHERE Estudios = %s LIMIT 100", (estudios,))
            else:
                cursor.execute("SELECT * FROM clientes_credito LIMIT 100")
            clientes = cursor.fetchall()
    finally:
        conexion.close()

    return jsonify(clientes)


@app.get("/clientes/estado-civil/<estado>")
def clientes_estado_civil(estado):
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM clientes_credito WHERE Estado_Civil=%s LIMIT 100",
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
                "SELECT * FROM clientes_credito WHERE Proposito=%s LIMIT 100",
                (proposito,)
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
                "SELECT * FROM clientes_credito WHERE Tipo_Jornada_Laboral=%s LIMIT 100",
                (jornada,)
            )
            clientes = cursor.fetchall()
    finally:
        conexion.close()

    return jsonify(clientes)

@app.get("/clientes/impago/<int:impago>")
def clientes_por_impago(impago):
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM clientes_credito WHERE Impago = %s LIMIT 100",
                (impago,)
            )
            clientes = cursor.fetchall()
    finally:
        conexion.close()

    return jsonify(clientes)

@app.delete("/clientes/<id>")
def eliminar_cliente(id):
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes_credito WHERE ID=%s", (id,))
            cliente = cursor.fetchone()
            if cliente is None:
                abort(404, description="Cliente no encontrado")
            
            cursor.execute("DELETE FROM clientes_credito WHERE ID=%s", (id,))
            conexion.commit()
    finally:
        conexion.close()
        
    return jsonify({"mensaje": f"Cliente con ID {id} eliminado exitosamente"})

@app.get("/creditos/indicadores-macro")
def obtener_indicadores_macro():
    url = "https://api.exchangerate-api.com/v4/latest/EUR"
    try:
        response = requests.get(url, timeout=5)
        
        response.raise_for_status()
        
        datos = response.json()
    
        return {
            "estado": "exitoso",
            "fuente_externa": "Exchange Rate API",
            "moneda_base": datos.get("base"),
            "fecha_actualizacion": datos.get("date"),
            "indicadores_clave": {
                "USD": datos.get("rates", {}).get("USD"),
                "GBP": datos.get("rates", {}).get("GBP"),
                "CHF": datos.get("rates", {}).get("CHF")
            }
        }, 200

    except requests.RequestException:
        abort(503, description="No se pudo obtener la información de la API externa de datos económicos")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)