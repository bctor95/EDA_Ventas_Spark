# Proyecto EDA_Ventas – Procesamiento Batch con Apache Spark

## Descripción General

Este proyecto implementa una aplicación en **Apache Spark** utilizando **Python (PySpark)** para realizar el **procesamiento batch** de un conjunto de datos de ventas.  
El propósito principal es aplicar conceptos de **Big Data** y **análisis exploratorio de datos (EDA)**, realizando tareas de limpieza, transformación y almacenamiento de información procesada de forma distribuida.

La solución permite demostrar el uso de Spark para ejecutar operaciones de análisis sobre grandes volúmenes de datos de manera eficiente, aplicando la metodología exigida en la **Fase 3 – Procesamiento de Datos con Apache Spark** del curso **Big Data (202016911A_2034)** de la **Universidad Nacional Abierta y a Distancia – UNAD Brayan Camilo Torres Torres**.

---

## Objetivo General
Implementar una aplicación en Apache Spark que procese, analice y almacene un conjunto de datos de manera distribuida, demostrando el funcionamiento del procesamiento batch con PySpark.

---

## Objetivos Específicos

- Cargar un conjunto de datos desde una fuente local (archivo CSV).
- Realizar tareas de limpieza y transformación utilizando DataFrames de PySpark.
- Aplicar operaciones de análisis exploratorio de datos (EDA).
- Generar y almacenar los resultados procesados en formato **Parquet**.
- Publicar el código fuente del proyecto en un repositorio GitHub con documentación y guía de ejecución.

---

## Tecnologías y Herramientas Utilizadas

- **Sistema Operativo:** Ubuntu (máquina virtual)
- **Lenguaje:** Python 3
- **Framework:** Apache Spark 3.x (PySpark)
- **Entorno de Ejecución:** PuTTY + VirtualBox
- **Control de Versiones:** Git y GitHub

---

## Instrucciones de Ejecución

1. Clonar el repositorio en el entorno local o servidor con Spark instalado:
   ```bash
   git clone https://github.com/bctor95/EDA_Ventas_Spark.git
   cd EDA_Ventas_Spark
2. Verificar la instalación de Spark:

spark-submit --version


3. Ejecutar la aplicación:

spark-submit ventas_eda.py

4. Esperar a que finalice la ejecución.
Se generará una carpeta llamada:

resultados/ventas_procesadas


5. Verificar los resultados procesados:

 ls resultados/ventas_procesadas

## Resultados Esperado

.Estructura del esquema del DataFrame.

.Cantidad de registros válidos procesados.

.Resumen estadístico de las variables numéricas.

.Agrupación de ventas por producto y por categoría.

.Archivos finales almacenados en formato Parquet.


## Autor
Brayan Camilo Torres Torres
Estudiante de Ingeniería de Sistemas

## Repositorio del Proyecto
 https://github.com/bctor95/EDA_Ventas_Spark

## Referencias
Macías, M. & Gómez, M. (2015). Introducción a Apache Spark: para empezar a programar el big data. Editorial UOC.

Montoya Suárez, L. & Gil Restrepo, G. A. (2018). Actualidad e importancia de la implementación de Big Data utilizando las herramientas Hadoop y Spark.

Maldonado, C. V. (2022). Analytics y Big Data. Ciencia de los Datos aplicada al mundo de los negocios. RIL editores.


