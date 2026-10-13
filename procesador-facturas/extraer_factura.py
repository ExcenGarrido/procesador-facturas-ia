import os
import json
from dotenv import load_dotenv
from groq import Groq

# 1. Cargar la API key desde el .env
load_dotenv()

# 2. Crear el cliente de Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 3. Texto de una factura real (desordenado, como llega de verdad)
factura_texto = """
Factura del proveedor Alimentos del Norte SRL
CUIT 20987654321
Nro B-0002-00005678
Fecha 18-01-2026
Azúcar 1kg x 20 ...... $30.000
IVA 21% incluido
Total final: $36.300
"""

# 4. El prompt: instrucciones claras para el LLM
prompt = f"""
Extraé los datos de esta factura y devolvelos como JSON con esta estructura exacta:

{{
    "proveedor": "nombre del proveedor",
    "cuit": "CUIT",
    "numero": "número de factura",
    "fecha": "fecha en formato DD-MM-YYYY",
    "total": 0.0
}}

Si no encontrás algún campo, poné null.

Factura:
{factura_texto}

Devolvé SOLO el JSON, sin texto adicional.
"""

# 5. Llamar a Groq
respuesta = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "Sos un asistente que extrae datos de facturas y responde solo en JSON."},
        {"role": "user", "content": prompt}
    ]
)

# 6. Extraer el texto de la respuesta
texto_respuesta = respuesta.choices[0].message.content

# 7. Convertir el texto a diccionario de Python
datos = json.loads(texto_respuesta)

# 8. Mostrar el resultado
print(datos)
print(f"\nProveedor: {datos['proveedor']}")
print(f"CUIT: {datos['cuit']}")
print(f"Total: ${datos['total']}")