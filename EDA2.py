# Importar pandas si no lo has hecho ya
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ver las primeras filas del dataset
df = pd.read_csv('vehiculos-de-segunda-mano-sample.csv')
df.head()
# Supongamos que 'precio' es la variable que queremos predecir
y = df['price']

# Distribución univariante de la variable precio
plt.figure(num="Distribución Univariante", figsize=(8,6))
sns.histplot(df['price'], kde=True)
plt.title("Distribución de la variable 'Precio'")
plt.xlabel("Precio")
plt.ylabel("Frecuencia")
plt.show()

# Estadísticas descriptivas de la variable precio
df['price'].describe()

# Boxplot para identificar outliers en la variable precio
plt.figure(num="Boxplot",figsize=(8,6))
sns.boxplot(df['price'])
plt.title("Boxplot de la variable 'Precio'")
plt.show()

# Diagrama de dispersión entre precio y kilometraje
plt.figure(num="Dispersión",figsize=(8,6))
sns.scatterplot(x=df['kms'], y=df['price'])
plt.title("Relación entre Kilometraje y Precio")
plt.xlabel("Kilometraje")
plt.ylabel("Precio")
plt.show()

# Gráfico de pares para analizar varias variables al mismo tiempo
sns.pairplot(df[['price', 'kms', 'year']])
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Hacer One-Hot Encoding de las variables categóricas
df_encoded = pd.get_dummies(df, columns=['doors', 'color'], drop_first=True)

# Seleccionar solo las columnas numéricas del DataFrame
df_numerico = df_encoded.select_dtypes(include=['float64', 'int64', 'uint8'])  # Ahora incluye las columnas 'one-hot'

# Crear el mapa de correlación solo con las columnas numéricas
plt.figure(figsize=(12, 10))
sns.heatmap(df_numerico.corr(), annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Mapa de correlación con variables categóricas codificadas")
plt.show()




