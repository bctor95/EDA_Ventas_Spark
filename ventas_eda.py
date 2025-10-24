
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, count as _count, avg

# 1. Crear la sesión de Spark
spark = SparkSession.builder.appName("EDA_Ventas").getOrCreate()

# 2. Cargar el dataset desde el archivo CSV
df = spark.read.csv("ventas.csv", header=True, inferSchema=True)

print("\n=== Esquema original de datos ===")
df.printSchema()

# 3. Limpieza y transformación
df_clean = df.dropna()
df_clean = df_clean.withColumnRenamed("producto_id", "id_producto")
df_clean = df_clean.withColumn("total", col("precio") * col("cantidad"))

# 4. Análisis exploratorio de datos (EDA)
print("\n=== Número total de registros limpios ===")
print(df_clean.count())

print("\n=== Resumen estadístico ===")
df_clean.describe().show()

print("\n=== Ventas totales por producto ===")
df_clean.groupBy("id_producto").agg(_sum("total").alias("ventas_totales")).orderBy(col("ventas_totales").desc()).show()

print("\n=== Métricas por categoría ===")
df_clean.groupBy("categoria").agg(
    _sum("total").alias("ventas_totales"),
    _count("*").alias("n_transacciones"),
    avg("total").alias("ticket_promedio")
).orderBy(col("ventas_totales").desc()).show()

# 5. Almacenar los resultados procesados en formato Parquet
df_clean.write.mode("overwrite").parquet("resultados/ventas_procesadas")

print("\n✅ Archivos Parquet generados en: resultados/ventas_procesadas")

spark.stop()
