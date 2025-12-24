import pandas as pd
import random
import os

def procesar_archivo_crudo(input_path, n_samples=20000):
    """
    Lee un CSV gigante y extrae una muestra aleatoria sin cargar todo en RAM.
    """
    print(f"Procesando: {input_path} ...")
    
    if not os.path.exists(input_path):
        print(f"Error: No encuentro el archivo {input_path}")
        return

    # 1. Contar filas totales
    print("   Contando filas totales...")
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        # Restamos 1 por la cabecera
        total_rows = sum(1 for line in f) - 1
    
    print(f"   Total de filas detectadas: {total_rows}")

    if total_rows < n_samples:
        print(f"   El archivo tiene menos de {n_samples} filas. Se copiará entero.")
        skip_indices = []
    else:
        # 2. Generar índices aleatorios para SALTAR
        print("   Calculando índices aleatorios...")
        rows_to_skip = total_rows - n_samples
        skip_indices = sorted(random.sample(range(1, total_rows + 1), rows_to_skip))

    # 3. Leer usando skiprows
    print("   Leyendo y extrayendo muestra...")
    df_sample = pd.read_csv(
        input_path, 
        skiprows=skip_indices, 
        low_memory=False,
        encoding='utf-8' 
    )

    # 4. Devolver resultado
    print(f"   Listo. {input_path} reducido a {len(df_sample)} filas.\n")
    return df_sample

# --- CONFIGURACIÓN ---
archivo_1 = "raw_data/accepted_2007_to_2018Q4.csv" 
archivo_2 = "raw_data/rejected_2007_to_2018Q4.csv"

# Ejecución
if __name__ == "__main__":
    df_acc = procesar_archivo_crudo(archivo_1, n_samples=20000)
    df_rej = procesar_archivo_crudo(archivo_2, n_samples=20000)

    df_final = pd.concat([df_acc, df_rej], ignore_index=True)
    print(f"DataFrame final combinado tiene {len(df_final)} filas.")
    df_final.to_csv("data/accepted_rejected_loans.csv", index=False)

    print("PROCESO TERMINADO.")