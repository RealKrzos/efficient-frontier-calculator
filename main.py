from Interface import input_stock_data
from Stock import Stock
from CorrelationCovarianceMatrix import CorrelationCovarianceMatrix
import matplotlib.pyplot as plt
import numpy as np


def plot_covariance_matrix(cov_matrix, stock_names):
    fig, ax = plt.subplots()
    cax = ax.matshow(cov_matrix, interpolation='nearest')
    fig.colorbar(cax)

    ax.set_xticklabels([''] + stock_names)
    ax.set_yticklabels([''] + stock_names)

    plt.title('Covariance Matrix Heatmap')
    plt.show()


def plot_stock_risk_return(stock_means, stock_stds):
    plt.figure(figsize=(10, 6))
    plt.scatter(stock_stds, stock_means, marker='o')
    plt.title('Stock Risk vs Return')
    plt.xlabel('Standard Deviation (Risk)')
    plt.ylabel('Mean Return')
    for i, txt in enumerate(range(len(stock_means))):
        plt.annotate(f'Stock {i + 1}', (stock_stds[i], stock_means[i]))
    plt.grid(True)
    plt.show()


def main():
    # Input stock data from the user
    stock_means, stock_stds = input_stock_data()

    # Create Stock instances
    stocks = [Stock(f"Stock{i + 1}", mean, std) for i, (mean, std) in enumerate(zip(stock_means, stock_stds))]

    # Create CorrelationCovarianceMatrix instance
    cor_cov_matrix = CorrelationCovarianceMatrix(stocks)

    # Assuming at least two stocks, set a correlation between the first two stocks for demonstration
    if len(stocks) > 1:
        cor_cov_matrix.add_correlation(stocks[0].name, stocks[1].name, 0.5)

    # Calculate the covariance matrix
    cov_matrix = cor_cov_matrix.calculate_covariance_matrix()

    # Plot the covariance matrix
    stock_names = [stock.name for stock in stocks]
    plot_covariance_matrix(cov_matrix, stock_names)

    # Plot stock risk vs return
    plot_stock_risk_return(stock_means, stock_stds)


if __name__ == "__main__":
    main()