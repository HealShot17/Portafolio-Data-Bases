# Limpieza de Datos: Precios de Viviendas

Este proyecto tiene como objetivo limpiar y preparar una base de datos de precios de viviendas para su análisis posterior. El conjunto de datos contiene información sobre propiedades inmobiliarias, incluyendo características como el tamaño del lote, la calidad de construcción, el año de construcción, entre otros.

## Estructura del Repositorio

- **`data/raw/`**: Contiene el archivo CSV original.
- **`data/cleaned/`**: Contiene el archivo CSV limpio después del procesamiento.
- **`notebooks/`**: Contiene el Jupyter Notebook con el proceso de limpieza.
- **`requirements.txt`**: Lista de dependencias necesarias para ejecutar el código.

## Proceso de Limpieza

1. **Carga de datos**: Se cargó el archivo CSV original utilizando `pandas`.
2. **Exploración de datos**: Se inspeccionaron los datos para identificar valores nulos, duplicados y errores.
3. **Limpieza de datos**:
   - Eliminación de columnas innecesarias.
   - Imputación de valores nulos.
   - Corrección de errores en los datos.
   - Conversión de tipos de datos.
4. **Guardado de datos limpios**: Los datos limpios se guardaron en un nuevo archivo CSV.

## Requisitos

Para ejecutar el código, asegúrate de tener instaladas las siguientes bibliotecas:

- `pandas`
- `numpy`

Puedes instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt