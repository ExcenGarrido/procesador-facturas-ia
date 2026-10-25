import os
import psycopg2
from dotenv import load_dotenv

# 1. Cargamos las variables de entorno desde el archivo .env
load_dotenv()

# 2. Simulamos el diccionario que nos devolvió el LLM (json.loads)
factura_ejemplo = {
    "proveedor": "Distribuidora Los Andes",
    "cuit": "30-1478785-8",
    "numero": "A-0001-00598765",
    "fecha": "2026-10-16",
    "total": 6050.75
}

# 3. Definimos la consulta SQL parametrizada (usando %s como marcadores)
sql_insert = """
INSERT INTO facturas (proveedor, cuit, numero, fecha, total)
VALUES (%s, %s, %s, %s, %s)
RETURNING id;
"""

# 4. Armamos la tupla de valores en el MISMO orden que las columnas del INSERT
valores = (
    factura_ejemplo["proveedor"],
    factura_ejemplo["cuit"],
    factura_ejemplo["numero"],
    factura_ejemplo["fecha"],
    factura_ejemplo["total"]
)

conexion = None
cursor = None

try:
    # 5. Abrimos la conexión al contenedor Docker de PostgreSQL
    conexion = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    cursor = conexion.cursor()

    # 6. Ejecutamos pasando la consulta por un lado y la tupla de datos por el otro
    cursor.execute(sql_insert, valores)

    # 7. Capturamos el ID autogenerado que nos devuelve RETURNING id
    id_generado = cursor.fetchone()[0]

    # 8. Confirmamos la transacción para que se guarde físicamente en la base
    conexion.commit()

    print(f"✅ Factura guardada con éxito en PostgreSQL. ID asignado: {id_generado}")

except psycopg2.Error as e:
    # 9. Si algo falla (ej. tabla inexistente o tipo de dato inválido), deshacemos cambios
    if conexion:
        conexion.rollback()
    print(f"❌ Error de base de datos al insertar la factura: {e}")

finally:
    # 10. Cerramos cursor y conexión siempre para no agotar la memoria del servidor
    if cursor:
        cursor.close()
    if conexion:
        conexion.close()