
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
paths:
  /:
   get:
    summary: Comprobar que funciona la API
    description: Comprueba que la API funciona correctamente
    parameters: no hay
    body: no hay
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

  /clientes:
   get:
    summary: Obtener clientes
    description: Obtiene una lista de 100 clientes almacenados en la base de datos
    parameters: no hay
    body: no hay
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
    body: no hay
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
    body: no hay
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
    body: no hay
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
    body: no hay
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
  /clientes/impago/<int:impago>
   get:
    summary: Obtener clientes por impago
    description: Permite filtrar clientes según si ha pagado o no.
    parameters: 
     - name: impago
       in: path
       required: true
       schema:
        type: string
       example: 1
    body: no hay
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
  /clientes/ingresos/<float:ingresos_min>
   get:
    summary: Obtener clientes por ingresos mínimos
    description: Permite filtrar clientes según su mínimo de ingresos.
    parameters: 
     - name: impago
       in: path
       required: true
       schema:
        type: string
       example: 1
    body: no hay
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
  