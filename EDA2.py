import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ver las primeras filas del dataset
df = pd.read_csv('vehiculos-de-segunda-mano-sample.csv')
df.head()
# Elegimos price como la variable predictora
y = df['price']

# ANALISIS UNIVARIANTE DE VARÍAS VARIABLES. PRECIO Q ES LA MÁS IMPORTANTE Y OTRAS QUE PUEDEN TENER UNA RELEVANCIA.

# Distribución univariante del precio
plt.figure(num="Distribución Univariante Precio", figsize=(8,6))
sns.histplot(df['price'], kde=True, color='blue')
plt.title("Distribución de la variable 'Precio'")
plt.xlabel("Precio")
plt.ylabel("Frecuencia")
plt.show()

# Distribución univariante del kilometraje
plt.figure(num="Distribución Univariante Kilometraje", figsize=(8,6))
sns.histplot(df['kms'], kde=True, color='green')
plt.title("Distribución de la variable 'Kilometraje'")
plt.xlabel("Kilometraje")
plt.ylabel("Frecuencia")
plt.show()

# Distribución univariante del año de fabricación
plt.figure(num="Distribución Univariante Año de Fabricación", figsize=(8,6))
sns.histplot(df['year'], kde=True, color='orange')
plt.title("Distribución de la variable 'Año de Fabricación'")
plt.xlabel("Año")
plt.ylabel("Frecuencia")
plt.show()

# Distribución de coches por provincia Top 10
plt.figure(num="Distribución de Coches por Provincia", figsize=(10, 6))
sns.countplot(data=df, x='location', order=df['location'].value_counts().index[:10], color='lightgreen')
plt.title("Distribución de Coches por Provincia (Top 10)")
plt.xlabel("Provincia")
plt.ylabel("Número de Coches")
plt.xticks(rotation=45)
plt.show()


# Estadísticas descriptivas de la variable precio
df['price'].describe()

# Boxplot para identificar outliers en la variable precio
plt.figure(num="Boxplot Precio", figsize=(8, 6))
sns.boxplot(df['price'])
plt.title("Boxplot de la variable 'Precio'")
plt.show()

# Boxplot para identificar outliers en la variable kilometraje
plt.figure(num="Boxplot Kilometraje", figsize=(8, 6))
sns.boxplot(df['kms'])
plt.title("Boxplot de la variable 'Kilometraje'")
plt.show()

# Boxplot para identificar outliers en el año de fabricación
plt.figure(num="Boxplot Año de Fabricación", figsize=(8, 6))
sns.boxplot(df['year'])
plt.title("Boxplot de la variable 'Año de Fabricación'")
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




