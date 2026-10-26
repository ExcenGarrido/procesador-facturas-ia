# 🧾 API & Pipeline de Procesamiento Inteligente de Facturas (IA + FastAPI)

Sistema automatizado de extremo a extremo (End-to-End) para la extracción, validación, persistencia y exposición de datos contables a partir de facturas en formato PDF y texto, utilizando Modelos de Lenguaje Grande (LLMs) y una arquitectura de API REST en la nube.

🌐 **Demo en vivo (Swagger UI en Azure):** [procesador-facturas.azurewebsites.net/docs](https://procesador-facturas-a8aag2exdzgghgb9.brazilsouth-01.azurewebsites.net/docs)

---

## 🚀 Arquitectura y Características Principales

- **Extracción Inteligente con IA (Groq API):** Procesamiento de documentos no estructurados (PDF y TXT) mediante LLMs para estructurar datos clave (proveedor, fecha, CUIT, número y totales) en formato JSON validado.
- **API RESTful con FastAPI:** Endpoints documentados bajo el estándar OpenAPI (Swagger) para consultar facturas procesadas, filtrar registros e integrar el servicio con sistemas externos.
- **Persistencia en Base de Datos SQL:** Modelado e inserción transaccional en PostgreSQL (`SQLAlchemy` + `psycopg2` con soporte SSL para Neon), garantizando integridad de datos y control de duplicados mediante consultas parametrizadas.
- **Procesamiento por Lotes:** Scripts automatizados para ingesta masiva de directorios de documentos (`pypdf`, `pathlib`).
- **Orquestación y Automatización:** Flujo de trabajo integrable con **n8n** (`flujo_n8n_facturas.json`) para automatización de procesos operativos.
- **Cloud & CI/CD:** Desplegado en **Microsoft Azure App Service (Linux)** con integración continua mediante **GitHub Actions**.

---

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python
- **Framework Web:** FastAPI, Uvicorn, Gunicorn
- **Inteligencia Artificial:** Groq SDK (LLMs)
- **Base de Datos & ORM:** PostgreSQL (Neon), SQLAlchemy, Psycopg2
- **Procesamiento de Archivos y Datos:** PyPDF, Pydantic, Python-Dotenv
- **Infraestructura & DevOps:** Azure App Service, GitHub Actions, n8n

---

## 📂 Estructura del Proyecto

- `api_facturas.py`: Punto de entrada de la API REST (FastAPI), configuración de SQLAlchemy y definición de endpoints de consulta.
- `extraer_factura.py`: Módulo de conexión con la API de Groq para extracción estructurada de datos desde texto/PDF.
- `procesar_lote_pdf.py` / `procesar_lote_txt.py`: Motores de procesamiento masivo por lotes con manejo de excepciones y transacciones seguras por archivo.
- `crear_tabla.py`: Script de inicialización del esquema relacional en la base de datos de producción.
- `insertar_factura.py`: Módulo de persistencia transaccional con consultas SQL parametrizadas.
- `listar_modelos.py`: Script de utilidad y diagnóstico para consultar modelos disponibles en la API de Groq.
- `flujo_n8n_facturas.json`: Plantilla exportable para automatización del flujo en n8n.

---

## 🔄 Capa de Automatización (n8n)

El proyecto incluye flujos de trabajo automatizados en **n8n** para consumir y procesar los datos expuestos por la API en la nube:

- **Consumo de Endpoints (`HTTP Request`)**: Se conecta de forma segura a la API desplegada en Azure para obtener el listado actualizado de facturas.
- **Procesamiento de Lotes (`Split Out`)**: Desglosa las respuestas JSON estructuradas en elementos individuales para su análisis unitario.
- **Evaluación de Negocio (`If`)**: Aplica reglas condicionales automáticas sobre los montos de las facturas (por ejemplo, filtrando transacciones que superen un determinado umbral).

El archivo JSON del flujo se encuentra disponible en el repositorio para su importación y ejecución directa.

---

## ⚙️ Instalación y Ejecución Local

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/ExcenGarrido/procesador-facturas-ia.git](https://github.com/ExcenGarrido/procesador-facturas-ia.git)
   cd procesador-facturas-ia

Instalar dependencias:

Bash
pip install -r requirements.txt
Configurar variables de entorno: Crear un archivo .env con las credenciales de PostgreSQL (DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT) y GROQ_API_KEY.

Iniciar el servidor de la API en desarrollo:

Bash
uvicorn api_facturas:app --reload


👤 Autor
Pablo Agustin Garrido

Técnico Universitario en Programación (UTN)

GitHub : https://github.com/ExcenGarrido