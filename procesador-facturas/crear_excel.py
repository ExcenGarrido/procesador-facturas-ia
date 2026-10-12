import pandas as pd

datos = {
    "numero": ["A-001", "A-002", "A-003"],
    "neto": [2500, "abc", 5000],
}

df = pd.DataFrame(datos)
df.to_excel("facturas.xlsx", index=False)