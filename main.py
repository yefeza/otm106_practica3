import pandas as pd
from matplotlib import pyplot as plt

# Grafica de ejemplo
eje_x = ["A", "B", "C", "D", "E"]
eje_y = [2, 3, 5, 7, 11]
fig, ax = plt.subplots()
ax.bar(eje_x, eje_y, color="blue", label="Datos de ejemplo")
fig.savefig("generados/grafica_ejemplo.png", bbox_inches="tight")

# Leer archivo Excel
archivo_excel = "datos/datos_base.xlsx"
contador = 1
while contador <= 5:
    data_hoja = pd.read_excel(archivo_excel, sheet_name=f"Hoja{contador}")
    print(f"Datos leidos de la Hoja{contador}")
    # Graficar datos de la hoja
    eje_x = data_hoja.iloc[:, 0]  # Asumiendo que la primera columna es el eje X
    eje_y = data_hoja.iloc[:, 1]  # Asumiendo que la segunda columna es el eje Y
    fig, ax = plt.subplots()
    ax.bar(eje_x, eje_y, color="green", label=f"Datos de Hoja {contador}")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_xticklabels(eje_x, rotation=45)
    ax.set_title(f"Gráfica de la Hoja {contador}")
    fig.savefig(f"generados/grafica_hoja_{contador}.png", bbox_inches="tight")
    contador = contador + 1
print("Gráficas generadas y guardadas en la carpeta 'generados'.")
