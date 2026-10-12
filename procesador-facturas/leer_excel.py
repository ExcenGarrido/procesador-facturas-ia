import pandas as pd

df = pd.read_excel("facturas.xlsx")

for index, row in df.iterrows():
    try:
        total = float(row["neto"]) * 1.21
        print(f"Fila {index}: {row['numero']} - Total: {total}")
    except ValueError:
        print(f"Fila {index}: {row['numero']} - Neto inválido: {row['neto']}")
        