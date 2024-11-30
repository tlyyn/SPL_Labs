import matplotlib.pyplot as plt
class MultiSubplots:
    def __init__(self, data):
        self.data = data

    def create_subplots(self, columns, plot_type='histogram', bins=10):
        num_plots = len(columns)
        fig, axs = plt.subplots(1, num_plots, figsize=(5 * num_plots, 5))

        for i, col in enumerate(columns):
            if plot_type == 'histogram':
                axs[i].hist(self.data[col], bins=bins, color='purple', alpha=0.7)
                axs[i].set_title(f'Гістограма {col}')
                axs[i].set_xlabel(col)
                axs[i].set_ylabel("Frequency")
            elif plot_type == 'scatter' and num_plots == 2:
                axs[i].scatter(self.data[columns[0]], self.data[columns[1]], color='blue', alpha=0.7)
                axs[i].set_title(f'Діаграма розсіювання {columns[0]} vs {columns[1]}')
                axs[i].set_xlabel(columns[0])
                axs[i].set_ylabel(columns[1])

        plt.tight_layout()
        plt.show()
