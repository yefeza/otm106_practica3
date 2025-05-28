import pandas as pd

archivo_excel = "datos/datos_base.xlsx"

data_hoja_1 = pd.read_excel(archivo_excel, sheet_name="Hoja1")

print(data_hoja_1)
