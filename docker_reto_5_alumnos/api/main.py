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
            cursor.execute("SELECT * FROM clientes_credito")
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
                cursor.execute("SELECT * FROM clientes_credito WHERE ID LIKE %s", (f"%{cliente_id}%",))
            elif estudios:
                cursor.execute("SELECT * FROM clientes_credito WHERE Estudios = %s", (estudios,))
            else:
                cursor.execute("SELECT * FROM clientes_credito")
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

@app.get("/clientes/impago/<int:impago>")
def clientes_por_impago(impago):
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM clientes_credito WHERE Impago = %s",
                (impago,)
            )
            clientes = cursor.fetchall()
    finally:
        conexion.close()

    return jsonify(clientes)

@app.get("/clientes/ingresos/<float:ingresos_min>")
def clientes_por_ingresos_min(ingresos_min):
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM clientes_credito WHERE Ingresos >= %s",
                (ingresos_min,)
            )
            clientes = cursor.fetchall()
    finally:
        conexion.close()

    return jsonify(clientes), 200

@app.post("/clientes")
def crear_cliente():
    datos = request.get_json(silent=True)
    
    if datos is None:
        abort(400, description="Datos de entrada incorrectos, debe ser un JSON valido")
    campos_obligatorios = ["ID", "Estudios", "Estado_Civil", "Proposito", "Tipo_Jornada_Laboral", "Ingresos", "Impago"]

    for campo in campos_obligatorios:
        if campo not in datos:
            abort(400, description=f"Falta el campo obligatorio: {campo}")

    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT ID FROM clientes_credito WHERE ID = %s", (datos["ID"],))
            if cursor.fetchone():
                abort(409, description=f"El cliente con ID {datos['ID']} ya existe")
            query = """
                INSERT INTO clientes_credito 
                (ID, Estudios, Estado_Civil, Proposito, Tipo_Jornada_Laboral, Ingresos, Impago)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                datos["ID"], 
                datos["Estudios"], 
                datos["Estado_Civil"], 
                datos["Proposito"], 
                datos["Tipo_Jornada_Laboral"], 
                datos["Ingresos"], 
                datos["Impago"]
            ))
            conexion.commit()
    finally:
        conexion.close()

    return jsonify(datos), 201

@app.patch("/clientes/<id>")
def modificar_cliente(id):
    datos = request.get_json(silent=True)
    if datos is None:
        abort(400, description="Datos de entrada incorrectos, debe ser un JSON valido")
    conexion = get_connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes_credito WHERE ID = %s", (id,))
            cliente = cursor.fetchone()
            if not cliente:
                abort(404, description=f"Cliente {id} no encontrado")

            estudios = datos.get("Estudios", cliente.get("Estudios"))
            estado_civil = datos.get("Estado_Civil", cliente.get("Estado_Civil"))
            proposito = datos.get("Proposito", cliente.get("Proposito"))
            jornada = datos.get("Tipo_Jornada_Laboral", cliente.get("Tipo_Jornada_Laboral"))
            ingresos = datos.get("Ingresos", cliente.get("Ingresos"))
            impago = datos.get("Impago", cliente.get("Impago"))

            query = """
                UPDATE clientes_credito 
                SET Estudios = %s, Estado_Civil = %s, Proposito = %s, 
                    Tipo_Jornada_Laboral = %s, Ingresos = %s, Impago = %s
                WHERE ID = %s
            """
            cursor.execute(query, (estudios, estado_civil, proposito, jornada, ingresos, impago, id))
            conexion.commit()
    finally:
        conexion.close()

    return jsonify({"mensaje": f"Cliente {id} modificado correctamente"}), 200

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
        
    return jsonify({"mensaje": f"Cliente {id} eliminado correctamente"})

@app.get("/cambio_moneda")
def obtener_indicadores_macro():
    url = "https://api.exchangerate-api.com/v4/latest/EUR"
    try:
        response = requests.get(
            url, timeout=5
            )
        response.raise_for_status()
        
        if response.status_code == 200:
            datos = response.json()
        else:
            print("Error")   
        return {
            "Resultado":"exitoso",
            "Api_externa":"Exchange Rate API",
            "moneda_base":datos.get("base"),
            "fecha_actualizacion":datos.get("date"),
            "indicadores_clave":{
                "USD": datos.get("rates", {}).get("USD"),
                "GBP": datos.get("rates", {}).get("GBP"),
                "CHF": datos.get("rates", {}).get("CHF")
            }
        }, 200
    except requests.RequestException:
        abort(503, description="No se pudo obtener la información de la API externa de cambio de moneda")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)