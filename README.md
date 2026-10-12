# Roadmap Python + IA

Repositorio de formación como desarrollador Python orientado a automatización con IA.
Incluye ejercicios de práctica y el desarrollo incremental de un procesador de facturas
con inteligencia artificial.

## Estructura

- `fase-0-ejercicios/`: ejercicios de calentamiento (fundamentos de Python).
- `procesador-facturas/`: proyecto real que se construye fase por fase.

## Fase 0 - Ejercicios

En `fase-0-ejercicios/`:

- `list_comprehensions.py`: ejercicios resueltos de list comprehensions.
- `metodos_clase.py`: clase `Producto` con métodos de instancia, clase y estático.
- `manejo_errores.py`: función `obtener_total` con manejo de `ValueError` y `KeyError`.

## Procesador de Facturas

En `procesador-facturas/`:

- `crear_excel.py`: genera un Excel de prueba con facturas.
- `leer_excel.py`: lee el Excel y procesa cada fila, manejando errores por fila sin detener el programa.

## Cómo ejecutar

Desde la raíz del repo, con el entorno virtual activado:

```bash
# Fase 0 - ejercicios
python fase-0-ejercicios/list_comprehensions.py
python fase-0-ejercicios/metodos_clase.py
python fase-0-ejercicios/manejo_errores.py

# Procesador de facturas
cd procesador-facturas
python crear_excel.py
python leer_excel.py
```

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

## Aprendizajes

1. Estructura de list comprehensions: `[expresión for elemento in iterable if condición]`.
2. La expresión es la parte más fácil de equivocar porque no da error pero el resultado es incorrecto.
3. `self` es la instancia específica; `cls` es la clase misma.
4. Los métodos de clase respetan la herencia usando `cls` en lugar de hardcodear el nombre.
5. Los métodos estáticos son funciones utilitarias que no dependen de la clase ni de la instancia.
6. Cada tipo de error necesita su propio `except` (`ValueError`, `KeyError`, `FileNotFoundError`).
7. `try/except` dentro de un bucle permite que un dato malo no rompa el procesamiento de los demás.

## Autor

Excen Garrido