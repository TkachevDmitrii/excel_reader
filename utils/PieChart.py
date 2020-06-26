import matplotlib.pyplot as plt


# Функция построения pie-chart
def build(name, sizes):

    # Значения для pie-chart
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'purple']
    explode = (0.1, 0, 0, 0, 0)  # explode 1st slice

    # Pie-chart
    plt.pie(sizes, explode=explode, labels=name, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    # Ось
    plt.axis('equal')

    return plt.show()
