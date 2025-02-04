# Limpieza de Datos: Precios de Viviendas

## 1. Importar Bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

## 2. Cargar los Datos
# Cargar el archivo CSV desde la carpeta 'data/raw/'
df = pd.read_csv('C:/Users/alber/OneDrive/Escritorio/Portafolio Data Bases/Portafolio-Data-Bases/House-Prices-Data-Cleaning/Data/raw/Datos.csv', quotechar='"')

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head())

# Información general del DataFrame
print("\nInformación del DataFrame:")
print(df.info())

## 3. Exploración de Datos
# Verificar valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Verificar valores duplicados
print("\nNúmero de filas duplicadas:", df.duplicated().sum())

# Estadísticas descriptivas de las columnas numéricas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Verificar valores únicos en columnas categóricas
print("\nValores únicos en columnas categóricas:")
for col in df.select_dtypes(include=['object']):
    print(f"{col}: {df[col].unique()}")

## 4. Limpieza de Datos
### 4.1. Eliminar Columnas Innecesarias
columnas_a_eliminar = ['Id', 'MiscFeature', 'PoolQC']
df_cleaned = df.drop(columns=columnas_a_eliminar)

print("\nColumnas eliminadas:", columnas_a_eliminar)

### 4.2. Manejar Valores Nulos
# Imputar valores nulos en columnas numéricas con la mediana
for col in df_cleaned.select_dtypes(include=['float64', 'int64']):
    df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)

# Imputar valores nulos en columnas categóricas con la moda
for col in df_cleaned.select_dtypes(include=['object']):
    df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)

print("\nValores nulos después de la imputación:")
print(df_cleaned.isnull().sum())

### 4.3. Eliminar Duplicados
df_cleaned = df_cleaned.drop_duplicates()

print("\nNúmero de filas después de eliminar duplicados:", df_cleaned.shape[0])

### 4.4. Corregir Tipos de Datos
# Convertir columnas de fecha
df_cleaned['YearBuilt'] = pd.to_datetime(df_cleaned['YearBuilt'], format='%Y')
df_cleaned['YearRemodAdd'] = pd.to_datetime(df_cleaned['YearRemodAdd'], format='%Y')

# Convertir columnas categóricas a tipo 'category'
for col in df_cleaned.select_dtypes(include=['object']):
    df_cleaned[col] = df_cleaned[col].astype('category')

print("\nTipos de datos después de la corrección:")
print(df_cleaned.dtypes)

### 4.5. Corregir Errores en los Datos
# Corregir errores en columnas de texto
df_cleaned['Street'] = df_cleaned['Street'].str.strip().str.lower()

# Reemplazar valores incorrectos en columnas categóricas
df_cleaned['GarageQual'] = df_cleaned['GarageQual'].replace(
    {'Po': 'Poor', 'Fa': 'Fair', 'TA': 'Average', 'Gd': 'Good', 'Ex': 'Excellent'}
)

print("\nValores únicos en 'GarageQual' después de la corrección:")
print(df_cleaned['GarageQual'].unique())

## 5. Guardado de Datos Limpios
# Crear la carpeta 'cleaned' si no existe
os.makedirs('c:/Users/alber/OneDrive/Escritorio/Portafolio Data Bases/Portafolio-Data-Bases/House-Prices-Data-/Data/Cleaned', exist_ok=True)

# Guardar los datos limpios en la carpeta 'data/cleaned/'
df_cleaned.to_csv('c:/Users/alber/OneDrive/Escritorio/Portafolio Data Bases/Portafolio-Data-Bases/House-Prices-Data/Data/Cleaned/Datos_Limpios.csv', index=False, quotechar='"')

print("\nDatos limpios guardados en 'data/cleaned/datos_limpios.csv'.")

## 6. Visualización de Resultados (Opcional)
# Histograma de la columna 'SalePrice'
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned['SalePrice'], kde=True, bins=30, color='blue')
plt.title('Distribución de Precios de Venta')
plt.xlabel('Precio de Venta')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de dispersión entre 'GrLivArea' y 'SalePrice'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='GrLivArea', y='SalePrice', data=df_cleaned, alpha=0.6, color='green')
plt.title('Relación entre Área Habitable y Precio de Venta')
plt.xlabel('Área Habitable (GrLivArea)')
plt.ylabel('Precio de Venta (SalePrice)')
plt.show()

## 7. Resumen del Proceso
print("Resumen de la limpieza:")
print(f"- Columnas originales: {df.shape[1]}")
print(f"- Columnas después de la limpieza: {df_cleaned.shape[1]}")
print(f"- Filas originales: {df.shape[0]}")
print(f"- Filas después de eliminar duplicados: {df_cleaned.shape[0]}")
print(f"- Valores nulos restantes: {df_cleaned.isnull().sum().sum()}")