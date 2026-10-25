import os
import json
import psycopg2

from groq import Groq
from dotenv import load_dotenv
from pypdf import PdfReader
from pypdf.errors import PdfStreamError
from pathlib import Path


load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

sql_insert = """
INSERT INTO facturas (proveedor, cuit, numero, fecha, total)
VALUES (%s, %s, %s, %s, %s)
RETURNING id;
"""

conexion = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
cursor = conexion.cursor()


carpeta_pdfs = Path(__file__).parent / "facturas_pdf"
archivos_pdf = sorted(carpeta_pdfs.glob("*.pdf"))

if not archivos_pdf:
    print("⚠️ No se encontraron archivos .pdf en la carpeta.")
else:
    print(f"📂 Se encontraron {len(archivos_pdf)} archivos. Procesando lote...\n")

    for ruta_pdf in archivos_pdf:
        try:
            print(f"📄 Leyendo PDF: {ruta_pdf.name}...")
            lector = PdfReader(ruta_pdf)

            paginas_texto = []
            for pagina in lector.pages:
               texto_pagina = pagina.extract_text()
               if texto_pagina:
                    paginas_texto.append(texto_pagina)

            texto_factura = "\n".join(paginas_texto).strip()

            if not texto_factura:
                            raise ValueError(
                                "No se pudo extraer texto (PDF en blanco o escaneado)."
                            )
            
            primera_linea = texto_factura.splitlines()[0]
            print(
                    f"   ✅ Extraído ({len(lector.pages)} pág. / {len(texto_factura)} caract.) -> '{primera_linea}'\n"
                 )

            
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
                            {texto_factura}
            
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
            
            
        except (OSError, PdfStreamError, ValueError, json.JSONDecodeError, psycopg2.Error) as e:
                        print(f"   ❌ Saltando '{ruta_pdf.name}': {e}\n")
                        conexion.rollback()

cursor.close()
conexion.close()