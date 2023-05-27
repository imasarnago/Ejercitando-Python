import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("problemas_graficos\\fechas_datos.csv")
# print (df)
# Creando el gráfico:
sns.lineplot(x="fecha", y="ganancia",data=df)
# Mostrando el gráfico:
plt.show()