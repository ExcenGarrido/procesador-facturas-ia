import os

from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv()

app = FastAPI(title="API Procesador de Facturas")


URL_DB = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
engine = create_engine(URL_DB)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True)
    proveedor = Column(String(255), nullable=False)
    cuit = Column(String(20))
    numero = Column(String(50))
    fecha = Column(Date)
    total = Column(Numeric(12, 2), nullable=False)



@app.get("/")
def inicio():
    return {
        "estado": "online",
        "sistema": "Procesador de Facturas",
        "mensaje": " servidor FastAPI está escuchando peticiones.",
    }

@app.get("/facturas")
def listar_facturas():
    sesion = SessionLocal()
    try:
        facturas = sesion.query(Factura).order_by(Factura.id.asc()).all()
        sesion.close()
        return {"cantidad": len(facturas), "facturas": facturas}
    except SQLAlchemyError as e:
        sesion.close()
        raise HTTPException(status_code=500, detail=f"Error en la base de datos: {e}")

@app.get("/facturas/{factura_id}")
def obtener_factura(factura_id: int):
    if factura_id <= 0:
        raise HTTPException(status_code=400, detail="El ID debe ser mayor a 0")

    sesion = SessionLocal()
    try:
        factura = sesion.query(Factura).filter(Factura.id == factura_id).first()
        sesion.close()

        if factura is None:
            raise HTTPException(
                status_code=404, detail=f"No existe la factura con ID {factura_id}"
            )

        return factura

    except SQLAlchemyError as e:
        sesion.close()
        raise HTTPException(
            status_code=500, detail=f"Error en la base de datos: {e}"
        )