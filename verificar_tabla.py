import os
import psycopg2
from dotenv import load_dotenv

# 1. Cargamos las variables de entorno
load_dotenv()

try:
    # 2. Conectamos a PostgreSQL en la nube (Neon) usando el .env y sslmode
    conexion = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT", 5432),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode="require"
    )

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'facturas'
        ORDER BY ordinal_position
    """)

    print("Columnas de la tabla 'facturas' en Neon:")
    for fila in cursor.fetchall():
        print(f"  - {fila[0]}: {fila[1]}")

    cursor.close()
    conexion.close()

except psycopg2.OperationalError as error:
    print(f"No se pudo conectar a PostgreSQL: {error}")