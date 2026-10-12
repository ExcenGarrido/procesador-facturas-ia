# Fase 0 - Calentamiento

Ejercicios de calentamiento antes del proyecto de automatización con IA.

## Contexto

Este repo es parte de un roadmap de formación como desarrollador Python
orientado a automatización con IA. La Fase 0 cierra gaps de fundamentos
antes de arrancar el proyecto real: un procesador de facturas con IA.

## Contenido

Todo el contenido de esta fase está en `fase-0-ejercicios/`:

- `list_comprehensions.py`: ejercicios resueltos de list comprehensions
- `metodos_clase.py`: clase `Producto` con métodos de instancia, clase y estático
- `manejo_errores.py`: función `obtener_total` con manejo de `ValueError` y `KeyError`

## Cómo ejecutar

Desde la raíz del repo:

```bash
python fase-0-ejercicios/list_comprehensions.py
python fase-0-ejercicios/metodos_clase.py
python fase-0-ejercicios/manejo_errores.py
```

## Aprendizajes

1. Estructura de list comprehensions: `[expresión for elemento in iterable if condición]`.
2. La expresión es la parte más fácil de equivocar porque no da error pero el resultado es incorrecto.
3. `self` es la instancia específica; `cls` es la clase misma.
4. Los métodos de clase respetan la herencia usando `cls` en lugar de hardcodear el nombre.
5. Los métodos estáticos son funciones utilitarias que no dependen de la clase ni de la instancia.
6. Cada tipo de error necesita su propio `except` (`ValueError`, `KeyError`, `FileNotFoundError`).

## Autor

Excen Garrido