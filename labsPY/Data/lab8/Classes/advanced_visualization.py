import matplotlib.pyplot as plt

class AdvancedVisualization:
    def __init__(self, data):
        self.data = data

    def scatter_plot(self, x_column, y_column, title="Діаграма розсіювання"):
        plt.figure(figsize=(8, 6))
        plt.scatter(self.data[x_column], self.data[y_column], c='blue', alpha=0.7)
        plt.title(title)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid()
        plt.show()

    def histogram(self, column, bins=10, title="Гістограма"):
        plt.figure(figsize=(8, 6))
        plt.hist(self.data[column], bins=bins, color='green', alpha=0.7)
        plt.title(title)
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.grid()
        plt.show()

    def pie_chart(self, column, title="Секторна діаграма"):
        data_counts = self.data[column].value_counts()
        plt.figure(figsize=(8, 6))
        plt.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.show()
