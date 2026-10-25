# 🧾 API & Pipeline de Procesamiento Inteligente de Facturas (IA + FastAPI)

Sistema automatizado de extremo a extremo (End-to-End) para la extracción, validación, persistencia y exposición de datos contables a partir de facturas en formato PDF y texto, utilizando Modelos de Lenguaje Grande (LLMs) y una arquitectura de API REST en la nube.

🌐 **Demo en vivo (Swagger UI en Azure):** [procesador-facturas.azurewebsites.net/docs](https://procesador-facturas-a8aag2exdzgghgb9.brazilsouth-01.azurewebsites.net/docs)

---

## 🚀 Arquitectura y Características Principales

- **Extracción Inteligente con IA (Groq API):** Procesamiento de documentos no estructurados (PDF y TXT) mediante LLMs para estructurar datos clave (proveedor, fecha, ítems, impuestos y totales) en formato JSON validado.
- **API RESTful con FastAPI:** Endpoints documentados bajo el estándar OpenAPI (Swagger) para consultar facturas procesadas, filtrar registros e integrar el servicio con sistemas externos.
- **Persistencia en Base de Datos SQL:** Modelado e inserción transaccional en PostgreSQL (`SQLAlchemy` + `psycopg2`), garantizando integridad de datos y control de duplicados.
- **Procesamiento por Lotes y Reportes:** Scripts automatizados para ingesta masiva de directorios (`pypdf`) y generación/lectura de reportes en Excel (`pandas`, `openpyxl`).
- **Orquestación y Automatización:** Flujo de trabajo integrable con **n8n** (`flujo_n8n_facturas.json`) para automatización de procesos operativos.
- **Cloud & CI/CD:** Desplegado en **Microsoft Azure App Service (Linux)** con integración continua mediante **GitHub Actions**.

---

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.13
- **Framework Web:** FastAPI, Uvicorn, Gunicorn
- **Inteligencia Artificial:** Groq SDK (LLMs)
- **Base de Datos & ORM:** PostgreSQL, SQLAlchemy, Psycopg2
- **Procesamiento de Archivos y Datos:** Pandas, OpenPyXL, PyPDF, FPDF2, Pydantic
- **Infraestructura & DevOps:** Azure App Service, GitHub Actions, Variables de Entorno (`python-dotenv`)

---

## 📂 Estructura del Proyecto

- `api_facturas.py`: Punto de entrada de la API REST (FastAPI), configuración de SQLAlchemy y definición de endpoints.
- `extraer_factura.py`: Módulo de conexión con la API de Groq para extracción estructurada de datos desde texto/PDF.
- `procesar_lote_pdf.py` / `procesar_lote_txt.py`: Motores de procesamiento masivo por lotes con manejo de excepciones por archivo.
- `conectar_db.py` / `crear_tabla.py` / `insertar_factura.py` / `verificar_tabla.py`: Capa de acceso a datos y gestión de tablas en PostgreSQL.
- `crear_excel.py` / `leer_excel.py`: Módulos de integración y exportación hacia planillas de cálculo.
- `flujo_n8n_facturas.json`: Plantilla exportable para automatización del flujo en n8n.

---

## ⚙️ Instalación y Ejecución Local

Clonar el repositorio:git clone https://github.com/ExcenGarrido/procesador-facturas-ia.gitcd procesador-facturas-ia

Instalar dependencias:pip install -r requirements.txt

Configurar variables de entorno: Crear un archivo .env con las credenciales de PostgreSQL (DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT) y GROQ_API_KEY.

Iniciar el servidor de la API:uvicorn api_facturas:app --reload

👤 Autor
Pablo Agustin Garrido

Técnico Universitario en Programación (UTN) 

GitHub: https://github.com/ExcenGarrido