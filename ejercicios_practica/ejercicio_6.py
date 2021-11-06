# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def pie_plot(x, y, z):
   
    fig = plt.figure()
    fig.suptitle('Ejemplo de Grafico de Torta', fontsize=16)
    ax = fig.add_subplot()

    index = y[z]
    ax.pie(x[index].values(), labels=x[index].keys(), autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    plt.show()
    print("Fin bar plot")

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    x = [{'carne':20, 'fruta':25, 'verdura':22},
         {'carne':23, 'fruta':23, 'verdura':18},
         {'carne':30, 'fruta':16, 'verdura':15},
         {'carne':26, 'fruta':21, 'verdura':20},
         ]
    y = {'Ene-Mar':0,'Abr-Jun':1,'Jul-Sep':2,'Oct-Dic':3}
    z = 'Ene-Mar'
    # Implementación:
     # Crear acá su gráfico
    pie_plot(x, y, z)
    print("terminamos")
