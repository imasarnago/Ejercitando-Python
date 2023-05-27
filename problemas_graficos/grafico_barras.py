import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("problemas_graficos\\ingresos.csv")
# print (df)

# Creando el gráfico:

sns.barplot(x="fuente", y="ingresos",data=df)

total_ingresos = df['ingresos'].sum()


# Mostrando el gráfico:

plt.show()