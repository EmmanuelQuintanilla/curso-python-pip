#Graficas para proyecto

import matplotlib.pyplot as plt

def generate_list(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values) #Funcion para crear graficas de barras
    plt.savefig("bar.png") #funcion para imprimir la grafica

def generate_pie(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels) #Funcion para crear graficas de pastel
    ax.axis("equal") #Funcion para que la grafica de pastel comience desde el centro
    plt.savefig("pie.png")

if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [75, 260, 150]
    #generate_list(labels, values)
    generate_pie(labels, values)
