import pandas as pd

def limpiar_reporte_ventas(archivo_entrada):
    # Cargar los datos
    print(f"Leyendo archivo: {archivo_entrada}")
    df = pd.read_excel(archivo_entrada)

    # 1. Eliminar filas completamente vacías
    df = df.dropna(how='all')

    # 2. Convertir nombres a mayúsculas para estandarizar
    if 'Nombre' in df.columns:
        df['Nombre'] = df['Nombre'].str.upper()

    # 3. Llenar valores nulos en columnas numéricas con 0
    df = df.fillna(0)

    # Guardar el resultado limpio
    df.to_excel("reporte_limpio.xlsx", index=False)
    print("¡Proceso terminado! Archivo guardado como reporte_limpio.xlsx")

# Este script demuestra habilidades de ETL (Extraer, Transformar y Cargar)
# fundamentales para el puesto de Analista/Programador BI.
