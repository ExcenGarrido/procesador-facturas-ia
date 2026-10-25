import os
import psycopg2
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

try:
    conexion = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT", 5432),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode="require"  # Requerido por Neon.tech para conexiones seguras en la nube
    )

    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS facturas (
            id SERIAL PRIMARY KEY,
            proveedor VARCHAR(200) NOT NULL,
            cuit VARCHAR(20),
            numero VARCHAR(50),
            fecha DATE,
            total NUMERIC(12, 2),
            creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conexion.commit()
    print("¡Tabla 'facturas' creada correctamente en la base de datos de Neon!")

    cursor.close()
    conexion.close()

except psycopg2.OperationalError as error:
    print(f"No se pudo conectar a PostgreSQL: {error}")