
#%%
#Esto genera una gráfica de la potencia de todos los coches
import pandas as pd
path = './data/vehiculos-de-segunda-mano-sample[1].csv'
csv = pd.read_csv(path)
power = csv["power"]
import matplotlib.pyplot as plt

# Graficar y ajustar los límites del eje Y
plt.figure(figsize=(12, 8))
plt.plot(csv['power'], marker='o', label='power')
plt.title('Gráfica de Potencias')
plt.xlabel('Índice')
plt.ylabel('Potencia')
# Ajustar los límites del eje Y (puedes cambiar los valores a tu necesidad)
plt.ylim(0, 1000)  # Limitar el eje Y a 10,000 (ajusta según tus datos)
plt.grid()
plt.legend()
plt.show()
#%%
#Esto genera una gráfica que muestra los kilometros de todos los coches
import pandas as pd
path = './data/vehiculos-de-segunda-mano-sample[1].csv'
csv = pd.read_csv(path)
kms = csv["kms"]
import matplotlib.pyplot as plt

# Graficar y ajustar los límites del eje Y
plt.figure(figsize=(12, 8))
plt.plot(csv['kms'], marker='o', label='kms')
plt.title('Gráfica de kilometros')
plt.xlabel('Índice')
plt.ylabel('Distancia Km')
# Ajustar los límites del eje Y (puedes cambiar los valores a tu necesidad)
plt.ylim(0, 1500000)  # Limitar el eje Y a 10,000 (ajusta según tus datos)
plt.grid()
plt.legend()
plt.show()
#%%
#Este genera un gráfico de barras comparando el tipo de combustible
import pandas as pd
path = './data/vehiculos-de-segunda-mano-sample[1].csv'
csv = pd.read_csv(path)
import matplotlib.pyplot as plt

fuel_counts = csv['fuel'].value_counts()

# Crear la gráfica de barras
plt.figure(figsize=(8, 6))
fuel_counts.plot(kind='bar', color=['yellow', 'brown', 'green'])

# Añadir títulos y etiquetas
plt.title('Cantidad de coches por tipo de combustible')
plt.xlabel('Tipo de combustible')
plt.ylabel('Cantidad')

# Mostrar la gráfica
plt.show()
#%%
#Este genera un gráfico de barras de que años son los coches
import pandas as pd
path = './data/vehiculos-de-segunda-mano-sample[1].csv'
csv = pd.read_csv(path)
import matplotlib.pyplot as plt

year_counts = csv['year'].value_counts()

# Crear la gráfica de barras
plt.figure(figsize=(8, 6))
year_counts.plot(kind='bar', color=['green', 'blue', 'red'])

# Añadir títulos y etiquetas
plt.title('Año del coche')
plt.xlabel('Año')
plt.ylabel('Cantidad')

# Mostrar la gráfica
plt.show()
#%%
#Este genera un gráfico de barras de si el coche es automatico o manual
import pandas as pd
path = './data/vehiculos-de-segunda-mano-sample[1].csv'
csv = pd.read_csv(path)
import matplotlib.pyplot as plt

shift_counts = csv['shift'].value_counts()

# Crear la gráfica de barras
plt.figure(figsize=(10, 8))
shift_counts.plot(kind='bar', color=['blue', 'purple'])

# Añadir títulos y etiquetas
plt.title('Tipo de cambio')
plt.xlabel('Automatico o manual')
plt.ylabel('Cantidad')

# Mostrar la gráfica
plt.show()
#%%
#La cantidad de coches que hay de cada marca
import pandas as pd
path = './data/vehiculos-de-segunda-mano-sample[1].csv'
csv = pd.read_csv(path)
import matplotlib.pyplot as plt

make_counts = csv['make'].value_counts()

# Crear la gráfica de barras
plt.figure(figsize=(10, 8))
make_counts.plot(kind='bar', color=['gray', 'brown', 'green', 'yellow', 'orange', 'red', 'blue'])

# Añadir títulos y etiquetas
plt.title('Marca de coche')
plt.xlabel('Marca')
plt.ylabel('Cantidad')

# Mostrar la gráfica
plt.show()
#%%
#El precio de cada coche
import pandas as pd
path = './data/vehiculos-de-segunda-mano-sample[1].csv'
csv = pd.read_csv(path)
import matplotlib.pyplot as plt

price_counts = csv['price'].value_counts()

# Crear la gráfica de barras
plt.figure(figsize=(10, 8))
plt.plot(csv['price'], marker='o', label='power')

# Añadir títulos y etiquetas
plt.title('Precio')
plt.xlabel('Precio')
plt.ylabel('Cantidad')

# Mostrar la gráfica
plt.show()
#%%
#Modelo del Coche
import pandas as pd
path = './data/vehiculos-de-segunda-mano-sample[1].csv'
csv = pd.read_csv(path)
import matplotlib.pyplot as plt

model_counts = csv['model'].value_counts()

# Crear la gráfica de barras
plt.figure(figsize=(120, 20))
model_counts.plot(kind='bar', color=['red', 'pink', 'yellow', 'purple', 'green', 'blue'])

# Añadir títulos y etiquetas
plt.title('Modelo del coche')
plt.xlabel('Modelo')
plt.ylabel('Cantidad')

# Mostrar la gráfica
plt.show()
#%%
