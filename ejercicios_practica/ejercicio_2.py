# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def multi_line_plot(x,y1,y2):
 
    # Calcular el gasto total como la suma
    # de las listas gasto_carne y gasto_verdura
    gasto_total = []
    for i in range(len(y1)):
        total = y2[i] + y1[i]
        gasto_total.append(total)

    # Realizaremos un gráfico "plot" con:
    # mes como "x"
    # gasto_carne como "y1"
    # gasto_cargasto_verdurane como "y2"
    # gasto_total como "y3"
    fig = plt.figure()
    fig.suptitle('Ejemplo Grafico MultiLineas', fontsize=16)
    ax = fig.add_subplot()

    ax.plot(x, y1, label='y1')
    ax.plot(x, y2, label='y2')
    ax.plot(x, gasto_total, label='y1 + y2')
    ax.legend()
    ax.grid()
    plt.show()
    print("Fin multi line plot")
    
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación ya está disponible, es la siguiente:
    x = list(np.linspace(-4, 4, 20))

    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)

    # Alumno: Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    # Crear acá su gráfico
    multi_line_plot(x,y1,y2)
    print("terminamos")
