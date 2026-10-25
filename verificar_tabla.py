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
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'facturas'
        ORDER BY ordinal_position
    """)

    print("Columnas de la tabla 'facturas':")
    for fila in cursor.fetchall():
        print(f"  - {fila[0]}: {fila[1]}")

    conexion.close()

except psycopg2.OperationalError as error:
    print(f"No se pudo conectar a PostgreSQL: {error}")