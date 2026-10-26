import os
import psycopg2
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

try:
    conexion = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT", 5432),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode="require"  # Esencial para conexiones seguras con Neon
    )
    
    cursor = conexion.cursor()
    cursor.execute("SELECT 1")
    resultado = cursor.fetchone()
    print(f"¡Conexión exitosa a la base de datos en Neon! Resultado de prueba: {resultado}")
    
    conexion.close()

except psycopg2.OperationalError as error:
    print(f"No se pudo conectar a PostgreSQL: {error}")