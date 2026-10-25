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
    cursor.execute("SELECT 1")
    resultado = cursor.fetchone()
    print(f"Conexión exitosa. Resultado de prueba: {resultado}")
    
    conexion.close()

except psycopg2.OperationalError as error:
    print(f"No se pudo conectar a PostgreSQL: {error}")