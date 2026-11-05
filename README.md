Objetivo 1:
Primero he leído el csv "Prestamos_educacion_limpio.csv".
Después he seleccionado las variables necesarias para calcular las cuotas y valorar la capacidad de pago: ingresos, ratio de deuda sobre ingresos, edad, posesión de hipoteca, importe del préstamo, tipo de interés y duración.
Con la edad y la posesión de hipoteca he creado la variable "Situacion_vivienda", para distinguir entre hipoteca, alquiler supuesto y ausencia de pago de vivienda. También he calculado los ingresos mensuales y las cuotas de los sistemas francés y alemán.
Después de eso he comparado el peso de cada cuota con los ingresos y con el endeudamiento que ya tiene cada persona. Según los límites establecidos para cada situación de vivienda, he asignado a cada préstamo el sistema francés o el alemán.
Por último, he creado cuadros de amortización de ejemplo y he calculado el VAN y la TIR de un préstamo de ejemplo, usando una tasa de descuento anual supuesta del 10 %.

Objetivo 2:
Para este objetivo he reutilizado los datos y el sistema de amortización elegidos en el objetivo 1. Primero he calculado el mes en que cada préstamo llega a la mitad y cuántas cuotas quedan pendientes.
Después he calculado el valor actual de esas cuotas. Para el sistema francés he usado una fórmula directa y, para el alemán, he descontado cada cuota pendiente. He comprobado el cálculo comparándolo con el saldo de los cuadros de amortización de un ejemplo de cada sistema.
Por último, he representado en gráficos la evolución de las cuotas y del saldo pendiente.

Objetivo 3:
Primero he leído el csv de "préstamos educación limpio";también he utilizado el de "prob_impago_train.csv" y "prob_impago_test.csv", que se habían generado con el modelo predictivo de impago del objetivo 4. He unido estos archivos con los datos de Educación usando la columna `ID`, manteniendo separados train y test.
Después he seleccionado las variables para predecir `Prima` y he excluido `Impago` real para que el modelo no use esa información como predictor. He ajustado una regresión lineal, revisado los p-valores y reducido las variables utilizadas.
A continuación he comparado modelos polinómicos de grados 3, 4 y 5 mediante validación cruzada. He elegido el grado 3 por ser más sencillo de explicar.
Por último he evaluado el modelo con el conjunto de test y he revisado sus predicciones.

Objetivos 4:
Primero he leído los dos csv el de prestamos y el de diccionarios.
Segundo he hecho una pequeña limpieza copiada del notebook de preprocesamiento.
Tercero he creado el modelo, entrenado y estandarizado.
Cuarto he visto con statsmodel los resultados y al no ser optimimos he regularizado con elasticNet.
Quinto he graficado los resultados y sacado conclusiones en el informe.
