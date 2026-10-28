
Este proyecto proporciona un entorno Docker con una base de datos MySQL ya preparada y cargada a partir de los datos disponibles en `datos/datos.xlsx`.

La base de datos utiliza almacenamiento persistente mediante un volumen Docker.

## Arranque

```bash
docker compose up --build
```

Servicios disponibles:

* API Flask: `http://localhost:8000`
* MySQL: `localhost:3306`
* Base de datos: `creditos`
* Usuario: `clase`
* Contraseña: `clase123`
* Tabla: `clientes_credito`

## Estructura

```text
.
├── api/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
│
├── datos/
│   └── datos.xlsx
│
├── loader/
│   ├── Dockerfile
│   ├── load_data.py
│   └── requirements.txt
│
├── docker-compose.yml
└── README.md
```

El trabajo sobre la API se realizará principalmente en:

```text
api/main.py
```

## Persistencia

Los datos de MySQL se almacenan en un volumen Docker y se mantienen aunque se detengan los contenedores:

```bash
docker compose down
```

Para volver a levantar el entorno:

```bash
docker compose up
```

Si se elimina el volumen:

```bash
docker compose down -v
```

la base de datos se volverá a generar a partir del fichero de datos en el siguiente arranque.

## Endpoints
### / (get)
```json
/:
  get:
    summary: Comprobar que funciona la API
    description: Comprueba que la API funciona correctamente
    parameters: no hay
    rquestBody: no hay
    responses: 
        '200':
          description: API operativa
          content:
            application/json:
              schema:
                type: object
                properties:
                  mensaje:
                    type: string
                    example: API funcionando
```
### /clientes (get)
```json
/clientes:
  get:
    summary: Obtener clientes
    description: Obtiene una lista de 100 clientes almacenados en la base de datos
    parameters: no hay
    requestBody: no hay
    responses: 
        '200':
          description: Consulta realizada correctamente
          content:
            application/json:
              schema:
                type: object
                properties:
                  ID:
                   type: string
                   example: FRMZVN
                  Edad:
                   type: integer
                   example: 35
                  Ingresos:
                   type: number
                   example: 44800
                  Monto_Inicial:
                   type: number
                   example: 63406
                  Scoring_Crediticio:
                   type: integer
                   example: 826
                  Meses_Empleo:
                   type: integer
                   example: 154
                  Num_Creditos:
                   type: integer
                   example: 2
                  Ratio_Interes:
                   type: number
                   example: 6,18
                  Duracion:
                   type: integer
                   example: 36
                  Ratio_Deuda_Ingresos:
                   type: number
                   example: 0.28
                  Estudios:
                   type: string
                   example: Máster
                  Tipo_Jornada_Laboral:
                   type: string
                   example: Jornada completa
                  Estado_Civil:
                   type: string
                   example: Casado
                  Posesion_Hipoteca:
                   type: integer
                   example: 1
                  Personas_Cargo:
                   type: integer
                   example: 0
                  Proposito:
                   type: string
                   example: Vivienda
                  Fiador:
                   type: integer
                   example: 0
                  Impago:
                   type: integer
                   example: 1
                  Prima:
                   type: number
                   example: 431,25
```
### /clientes/buscar (get)
```json
/clientes/buscar:
 get:
    summary: Buscar clientes
    description: Permite filtrar por ID o Estudios
    parameters: 
     - name: id
       in: query
       required: false
       schema:
        type: string
       example: YBJXM9
     - name: estudios
       in: query
       required: false
       schema:
        type: string
       example: Grado Universitario
    requestBody: no hay
    responses: 
        '200':
          description: Consulta realizada correctamente
          content:
            application/json:
              schema:
                type: object
                properties:
                  ID:
                   type: string
                   example: YBJXM9
                  Edad:
                   type: integer
                   example: 35
                  Ingresos:
                   type: number
                   example: 44800
                  Monto_Inicial:
                   type: number
                   example: 63406
                  Scoring_Crediticio:
                   type: integer
                   example: 826
                  Meses_Empleo:
                   type: integer
                   example: 154
                  Num_Creditos:
                   type: integer
                   example: 2
                  Ratio_Interes:
                   type: number
                   example: 6,18
                  Duracion:
                   type: integer
                   example: 36
                  Ratio_Deuda_Ingresos:
                   type: number
                   example: 0.28
                  Estudios:
                   type: string
                   example: Grado Universitario
                  Tipo_Jornada_Laboral:
                   type: string
                   example: Jornada completa
                  Estado_Civil:
                   type: string
                   example: Casado
                  Posesion_Hipoteca:
                   type: integer
                   example: 1
                  Personas_Cargo:
                   type: integer
                   example: 0
                  Proposito:
                   type: string
                   example: Vivienda
                  Fiador:
                   type: integer
                   example: 0
                  Impago:
                   type: integer
                   example: 1
                  Prima:
                   type: number
                   example: 431,25
```
### /clientes/estado-civil/<estado> (get)
```json
/clientes/estado-civil/<estado>:
  get:
    summary: Obtener clientes por estado civil
    description: Permite filtrar clientes según su estado civil.
    parameters: 
     - name: estado
       in: path
       required: true
       schema:
        type: string
       example: Casado
    requestBody: no hay
    responses: 
        '200':
          description: Consulta realizada correctamente
          content:
            application/json:
              schema:
                type: object
                properties:
                  ID:
                   type: string
                   example: FRMZVN
                  Edad:
                   type: integer
                   example: 35
                  Ingresos:
                   type: number
                   example: 44800
                  Monto_Inicial:
                   type: number
                   example: 63406
                  Scoring_Crediticio:
                   type: integer
                   example: 826
                  Meses_Empleo:
                   type: integer
                   example: 154
                  Num_Creditos:
                   type: integer
                   example: 2
                  Ratio_Interes:
                   type: number
                   example: 6,18
                  Duracion:
                   type: integer
                   example: 36
                  Ratio_Deuda_Ingresos:
                   type: number
                   example: 0.28
                  Estudios:
                   type: string
                   example: Máster
                  Tipo_Jornada_Laboral:
                   type: string
                   example: Jornada completa
                  Estado_Civil:
                   type: string
                   example: Casado
                  Posesion_Hipoteca:
                   type: integer
                   example: 1
                  Personas_Cargo:
                   type: integer
                   example: 0
                  Proposito:
                   type: string
                   example: Vivienda
                  Fiador:
                   type: integer
                   example: 0
                  Impago:
                   type: integer
                   example: 1
                  Prima:
                   type: number
                   example: 431,25
```
### /clientes/proposito/<proposito> (get)
```json
/clientes/proposito/<proposito>
  get:
    summary: Obtener clientes por proposito
    description: Permite filtrar clientes según su proposito.
    parameters: 
     - name: proposito
       in: path
       required: true
       schema:
        type: string
       example: Vivienda
    requestBody: no hay
    responses: 
        '200':
          description: Consulta realizada correctamente
          content:
            application/json:
              schema:
                type: object
                properties:
                  ID:
                   type: string
                   example: FRMZVN
                  Edad:
                   type: integer
                   example: 35
                  Ingresos:
                   type: number
                   example: 44800
                  Monto_Inicial:
                   type: number
                   example: 63406
                  Scoring_Crediticio:
                   type: integer
                   example: 826
                  Meses_Empleo:
                   type: integer
                   example: 154
                  Num_Creditos:
                   type: integer
                   example: 2
                  Ratio_Interes:
                   type: number
                   example: 6,18
                  Duracion:
                   type: integer
                   example: 36
                  Ratio_Deuda_Ingresos:
                   type: number
                   example: 0.28
                  Estudios:
                   type: string
                   example: Máster
                  Tipo_Jornada_Laboral:
                   type: string
                   example: Jornada completa
                  Estado_Civil:
                   type: string
                   example: Casado
                  Posesion_Hipoteca:
                   type: integer
                   example: 1
                  Personas_Cargo:
                   type: integer
                   example: 0
                  Proposito:
                   type: string
                   example: Vivienda
                  Fiador:
                   type: integer
                   example: 0
                  Impago:
                   type: integer
                   example: 1
                  Prima:
                   type: number
                   example: 431,25
```
### clientes/jornada/<jornada> (get)
```json
/clientes/jornada/<jornada>
  get:
    summary: Obtener clientes por jornada
    description: Permite filtrar clientes según su jornada laboral.
    parameters: 
     - name: jornada
       in: path
       required: true
       schema:
        type: string
       example: Jornada completa
    requestBody: no hay
    responses: 
        '200':
          description: Consulta realizada correctamente
          content:
            application/json:
              schema:
                type: object
                properties:
                  ID:
                   type: string
                   example: FRMZVN
                  Edad:
                   type: integer
                   example: 35
                  Ingresos:
                   type: number
                   example: 44800
                  Monto_Inicial:
                   type: number
                   example: 63406
                  Scoring_Crediticio:
                   type: integer
                   example: 826
                  Meses_Empleo:
                   type: integer
                   example: 154
                  Num_Creditos:
                   type: integer
                   example: 2
                  Ratio_Interes:
                   type: number
                   example: 6,18
                  Duracion:
                   type: integer
                   example: 36
                  Ratio_Deuda_Ingresos:
                   type: number
                   example: 0.28
                  Estudios:
                   type: string
                   example: Máster
                  Tipo_Jornada_Laboral:
                   type: string
                   example: Jornada completa
                  Estado_Civil:
                   type: string
                   example: Casado
                  Posesion_Hipoteca:
                   type: integer
                   example: 1
                  Personas_Cargo:
                   type: integer
                   example: 0
                  Proposito:
                   type: string
                   example: Vivienda
                  Fiador:
                   type: integer
                   example: 0
                  Impago:
                   type: integer
                   example: 1
                  Prima:
                   type: number
                   example: 431,25
```
### clientes/impago/<int:impago> (get)
```json
/clientes/impago/<int:impago>
  get:
    summary: Obtener clientes por impago
    description: Permite filtrar clientes según si ha pagado o no.
    parameters: 
     - name: impago
       in: path
       required: true
       schema:
        type: integer
       example: 1
    requestBody: no hay
    responses: 
        '200':
          description: Consulta realizada correctamente
          content:
            application/json:
              schema:
                type: object
                properties:
                  ID:
                   type: string
                   example: FRMZVN
                  Edad:
                   type: integer
                   example: 35
                  Ingresos:
                   type: number
                   example: 44800
                  Monto_Inicial:
                   type: number
                   example: 63406
                  Scoring_Crediticio:
                   type: integer
                   example: 826
                  Meses_Empleo:
                   type: integer
                   example: 154
                  Num_Creditos:
                   type: integer
                   example: 2
                  Ratio_Interes:
                   type: number
                   example: 6,18
                  Duracion:
                   type: integer
                   example: 36
                  Ratio_Deuda_Ingresos:
                   type: number
                   example: 0.28
                  Estudios:
                   type: string
                   example: Máster
                  Tipo_Jornada_Laboral:
                   type: string
                   example: Jornada completa
                  Estado_Civil:
                   type: string
                   example: Casado
                  Posesion_Hipoteca:
                   type: integer
                   example: 1
                  Personas_Cargo:
                   type: integer
                   example: 0
                  Proposito:
                   type: string
                   example: Vivienda
                  Fiador:
                   type: integer
                   example: 0
                  Impago:
                   type: integer
                   example: 1
                  Prima:
                   type: number
                   example: 431,25
```
### /clientes/ingresos/<float:ingresos_min> (get)
```json
/clientes/ingresos/<float:ingresos_min>
  get:
    summary: Obtener clientes por ingresos mínimos
    description: Permite filtrar clientes según su mínimo de ingresos.
    parameters: 
     - name: ingresos_min
       in: path
       required: true
       schema:
        type: number
        format: float
       example: 44800
    requestBody: no hay
    responses: 
        '200':
          description: Consulta realizada correctamente
          content:
            application/json:
              schema:
                type: object
                properties:
                  ID:
                   type: string
                   example: FRMZVN
                  Edad:
                   type: integer
                   example: 35
                  Ingresos:
                   type: number
                   example: 44800
                  Monto_Inicial:
                   type: number
                   example: 63406
                  Scoring_Crediticio:
                   type: integer
                   example: 826
                  Meses_Empleo:
                   type: integer
                   example: 154
                  Num_Creditos:
                   type: integer
                   example: 2
                  Ratio_Interes:
                   type: number
                   example: 6,18
                  Duracion:
                   type: integer
                   example: 36
                  Ratio_Deuda_Ingresos:
                   type: number
                   example: 0.28
                  Estudios:
                   type: string
                   example: Máster
                  Tipo_Jornada_Laboral:
                   type: string
                   example: Jornada completa
                  Estado_Civil:
                   type: string
                   example: Casado
                  Posesion_Hipoteca:
                   type: integer
                   example: 1
                  Personas_Cargo:
                   type: integer
                   example: 0
                  Proposito:
                   type: string
                   example: Vivienda
                  Fiador:
                   type: integer
                   example: 0
                  Impago:
                   type: integer
                   example: 1
                  Prima:
                   type: number
                   example: 431,25
```
### clientes (post)
```json
/clientes:
  post:
    summary: Crear cliente
    description: Crea un nuevo cliente en la base de datos.
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - ID
              - Estudios
              - Estado_Civil
              - Proposito
              - Tipo_Jornada_Laboral
              - Ingresos
              - Impago
            properties:
              ID:
                type: string
                example: 4UO7DJ
              Estudios:
                type: string
                example: Grado Universitario
              Estado_Civil:
                type: string
                example: Soltero
              Proposito:
                type: string
                example: Negocios
              Tipo_Jornada_Laboral:
                type: string
                example: Tiempo parcial
              Ingresos:
                type: number
                example: 34325
              Impago:
                type: integer
                example: 0
    responses:
      '201':
        description: Cliente creado correctamente
      '400':
        description: Datos de entrada incorrectos
      '409':
        description: El cliente ya existe
```
### /clientes/<id> (patch)
```json
/clientes/<id>:
  patch:
     summary: Actualizar cliente
     description: Modifica los datos de un cliente existente.
     parameters: 
      - name: ID
        in: path
        required: true
        schema:
         type: string
        example: 7XD0MJ
     requestBody:
      required: true
      content:
       application/json:
        schema:
         type: object
         properties:
          Estudios:
           type: string
           example: Doctorado
          Estado_Civil:
           type: string
           example: Soltero
          Proposito:
           type: string
           example: Educación
          Tipo_Jornada_Laboral:
           type: string
           example: Autónomo
          Ingresos:
           type: number
           example: 63033
          Impago:
           type: integer
           example: 1
     responses:
         '200':
          description: Cliente modificado correctamente
         '400':
          description: Datos de entrada incorrectos
         '404':
          description: Cliente no encontrado
```
### /clientes/<id> (delete)
```json
/clientes/<id>:
  delete:
     summary: Eliminar cliente
     description: Borra un cliente de la base de datos a partir de su ID.
     parameters: 
      - name: id
        in: path
        required: true
        schema:
         type: string
        example: 98XK3H
     requestBody: no hay
     responses:
         '200':
          description: Cliente eliminado correctamente
         '404':
          description: Cliente no encontrado
```
### /cambio_moneda (get)
```json
/cambio_moneda:
  get:
     summary: Obtiene tipo de cambio
     description: Utiliza una API externa para obtener las tasas de cambio actuales respecto al Euro.
     parameters: no hay
     requestBody: no hay
     responses: 
         '200':
          description: Consulta a la API externa realizada con éxito
          content:
           application/json:
            schema:
             type: object
             properties:
              Resultado:
               type: string
               example: exitoso
              Api_externa:
               type: string
               example: Exchange Rate API
              moneda_base:
               type: string
               example: EUR
              fecha_actualizacion:
               type: string
               example: 2026-03-30
              indicadores_clave:
               type: object
               properties:
                USD:
                 type: number
                 example: 1.08
                GBP:
                 type: number
                 example: 0.85
                CHF:
                 type: number
                 example: 0.97
         '503':
          description: No se pudo obtener la información de la API externa
```
## Gestión de errores
Todas las respuestas de error de la API devuelven un objeto JSON con una estructura estándar que incluye el código de estado y un mensaje descriptivo:
### Error 400 - Bad Request
```json
{
  "error": {
    "code": 400,
    "message": "Datos de entrada incorrectos"
  }
}
```
### Error 404 - Not Found
```json
{
  "error": {
    "code": 404,
    "message": "El recurso no existe"
  }
}
```
### Error 405 - Method Not Allowed
```json
{
  "error": {
    "code": 405,
    "message": "Metodo no permitido"
  }
}
```
### Error 409 - Conflict
```json
{
  "error": {
    "code": 409,
    "message": "Conflicto con el estado actual"
  }
}
```
### Error 415 - Unsupported Media Type
```json
{
  "error": {
    "code": 415,
    "message": "Formato recibido no soportado"
  }
}
```
### Error 500 - Internal Server Error
```json
{
  "error": {
    "code": 500,
    "message": "Error inesperado en el servidor"
  }
}
```