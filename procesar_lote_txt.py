from pathlib import Path
import os
import json
import psycopg2
from dotenv import load_dotenv
from groq import Groq

# --- Inicialización y conexiones ---
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

sql_insert = """
INSERT INTO facturas (proveedor, cuit, numero, fecha, total)
VALUES (%s, %s, %s, %s, %s)
RETURNING id;
"""

# Añadimos sslmode="require" para garantizar compatibilidad con Neon en la nube
conexion = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT", 5432),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    sslmode="require"
)
cursor = conexion.cursor()

# --- LECTURA DE LA CARPETA ---
carpeta_facturas = Path(__file__).parent / "facturas_txt"
archivos_txt = sorted(carpeta_facturas.glob("*.txt"))

if not archivos_txt:
    print("⚠️ No se encontraron archivos .txt en la carpeta.")
else:
    print(f"📂 Se encontraron {len(archivos_txt)} archivos. Procesando lote...\n")

    for ruta_archivo in archivos_txt:
        try:
            print(f"📄 Archivo detectado: {ruta_archivo.name}")
            texto = ruta_archivo.read_text(encoding="utf-8").strip()

            if not texto:
                raise ValueError("El archivo está vacío (0 caracteres).")
        
            prompt = f"""
                Extraé los datos de esta factura y devolvelos como JSON con esta estructura exacta:

                {{
                "proveedor": "nombre del proveedor",
                "cuit": "CUIT",
                "numero": "número de factura",
                "fecha": "fecha en formato YYYY-MM-DD",
                "total": 0.0
                }}

                Si no encontrás algún campo, poné null.

                Factura:
                {texto}

                Devolvé SOLO el JSON, sin texto adicional.
                """

            respuesta = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {"role": "system", "content": "Sos un asistente que extrae datos de facturas y responde solo en JSON."},
                    {"role": "user", "content": prompt}
                ]
            ) 
            texto_respuesta = respuesta.choices[0].message.content
            datos_factura = json.loads(texto_respuesta)
            print(datos_factura)

            valores = (
                datos_factura["proveedor"],
                datos_factura["cuit"],
                datos_factura["numero"],
                datos_factura["fecha"],
                datos_factura["total"]
             )

            cursor.execute(sql_insert, valores)  
            id_generado = cursor.fetchone()[0]
            conexion.commit()
            print(f"   ✅ Guardada en PostgreSQL con ID: {id_generado}\n")

        except (OSError, UnicodeDecodeError, ValueError, json.JSONDecodeError, psycopg2.Error) as e:
            print(f"   ❌ Saltando '{ruta_archivo.name}': {e}\n")
            conexion.rollback()

cursor.close()
conexion.close()