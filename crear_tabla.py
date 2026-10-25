import psycopg2

try:
    conexion = psycopg2.connect(
        host="localhost",
        port=5432,
        database="facturas",
        user="admin",
        password="admin123"
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
    print("Tabla 'facturas' creada correctamente.")

    conexion.close()

except psycopg2.OperationalError as error:
    print(f"No se pudo conectar a PostgreSQL: {error}")

