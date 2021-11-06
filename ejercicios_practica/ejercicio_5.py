# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def bar_plot(x, y):
   
    fig = plt.figure()
    fig.suptitle('Ejemplo de Grafico de Barras', fontsize=16)
    ax = fig.add_subplot()

    ax.bar(x, y, label='datos')
    ax.legend()
    ax.grid()
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
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Crear acá su gráfico
    bar_plot(x, y1)
    bar_plot(x, y2)
    bar_plot(x, y3)
    bar_plot(x, y4)
    x1 = ['Ene-Mar','Abr-Jun', 'Jul-Sep','Oct-Dic']
    y1 = [25, 23, 16, 21]
    bar_plot(x1, y1)
    print("terminamos")
