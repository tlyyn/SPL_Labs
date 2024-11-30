import matplotlib.pyplot as plt

class BasicVisualization:
    def __init__(self, data):
        self.data = data

    def line_plot(self, x_column, y_column, title="Лінійний графік"):
        plt.figure(figsize=(8, 6))
        plt.plot(self.data[x_column], self.data[y_column], marker='o')
        plt.title(title)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid()
        plt.show()
