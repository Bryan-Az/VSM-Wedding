import matplotlib.pyplot as plt

def plot_data(data, column):
    """
    Plot a histogram of the data for a specific column.
    """
    plt.hist(data[column])
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
