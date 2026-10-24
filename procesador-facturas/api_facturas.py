import os
import json
import psycopg2 

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv()
app = FastAPI(title="API Procesador de Facturas")

def obtener_conexion():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.get("/")
def inicio():
    return {
        "estado": "online",
        "sistema": "Procesador de Facturas",
        "mensaje": " servidor FastAPI está escuchando peticiones.",
    }

@app.get("/facturas")
def listar_facturas():
    try:


        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, proveedor, cuit, numero, fecha, total FROM facturas ORDER BY id ASC;")
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()

        facturas = []

        for fila in filas:
                facturas.append({
                "id": fila[0],
                "proveedor": fila[1],
                "cuit": fila[2],
                "numero": fila[3],
                "fecha": str(fila[4]),    # Convertimos la fecha a texto "YYYY-MM-DD"
                "total": float(fila[5])   # Convertimos el NUMERIC a float para JSON
                
        })
        return {"cantidad": len(facturas), "facturas": facturas}

    
    except psycopg2.Error as e:
         raise HTTPException(status_code=500, detail=f"Error en la base de datos: {e}")

@app.get("/facturas/{factura_id}")
def obtener_factura(factura_id: int):
   if factura_id <= 0:
      raise HTTPException(status_code=400, detail="El ID debe ser mayor a 0")

   try:
       
       conexion = obtener_conexion()
       cursor = conexion.cursor()

       cursor.execute(
       "SELECT id, proveedor, cuit, numero, fecha, total FROM facturas WHERE id = %s;",
       (factura_id,)
       )
       
       fila = cursor.fetchone()
       cursor.close()
       conexion.close()

       if fila is None:
           raise HTTPException(status_code=404, detail=f"No existe la factura con ID {factura_id}")
       
       return  {"id": fila[0], "proveedor": fila[1], "cuit": fila[2], "numero": fila[3], "fecha": str(fila[4]), "total": float(fila[5])}

   except psycopg2.Error as e:
       raise HTTPException(status_code=500, detail=f"Error en la base de datos: {e}") 
