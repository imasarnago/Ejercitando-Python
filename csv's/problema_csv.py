import pandas as pd

df = pd.read_csv("csv's\\datos.csv")

# Convertir a string los datos de una columna :

df_edad = df['edad'].astype(str)

# Me reemplaza en la columna nombre, "ima" con "nol". Inplace me modifica el archivo original

df["nombre"].replace ("ima","nol",inplace=True)


print (df)
# Elimina las filas que tienen celdas vacías
df = df.dropna()
# Elimina las columnas que tienen celdas vacías
df = df.dropna(axis=1)

# Elimina las filas que tienen filas duplicadas
df = df.drop_duplicates()

df.to_csv("csv's\\datos_limpios.csv")


# Eso me crea el nuevo archivo, limpio. Funciona!!