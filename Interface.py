import numpy as np

def input_stock_data():
    num_stocks = int(input("Enter the number of stocks: "))
    stock_means = []
    stock_stds = []

    for i in range(num_stocks):
        mean = float(input(f"Enter mean return for Stock {i + 1}: "))
        std = float(input(f"Enter standard deviation for Stock {i + 1}: "))
        stock_means.append(mean)
        stock_stds.append(std)

    return np.array(stock_means), np.array(stock_stds)


# Example usage
stock_means, stock_stds = input_stock_data()
# You would need to modify how correlation_matrix and cov_matrix are handled based on user input
