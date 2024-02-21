import numpy as np
import matplotlib.pyplot as plt

# Define the expected returns and standard deviations for each stock
stock_means = np.array([0.08, 0.12, 0.10])  # Mean returns for Stocks A, B, C
stock_stds = np.array([0.15, 0.20, 0.18])  # Standard deviations for Stocks A, B, C
correlation_matrix = np.array([[1, 0.2, 0.1], [0.2, 1, 0.3], [0.1, 0.3, 1]])  # Simplified correlation matrix

# Calculate the covariance matrix based on standard deviations and correlation matrix
cov_matrix = np.outer(stock_stds, stock_stds) * correlation_matrix

# Number of random portfolios
num_portfolios = 10000

# Initialize arrays to store portfolio returns, standard deviations, and weights
portfolio_means = np.zeros(num_portfolios)
portfolio_stds = np.zeros(num_portfolios)
portfolio_weights = np.zeros((num_portfolios, len(stock_means)))

# Generate random portfolios
np.random.seed(42)  # For reproducible results
for i in range(num_portfolios):
    weights = np.random.random(len(stock_means))
    weights /= np.sum(weights)  # Normalize weights to sum to 1
    portfolio_weights[i] = weights

    # Calculate expected portfolio return
    portfolio_means[i] = np.sum(weights * stock_means)

    # Calculate portfolio standard deviation
    portfolio_stds[i] = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

# Plot the portfolios
plt.figure(figsize=(10, 6))
plt.scatter(portfolio_stds, portfolio_means, c=portfolio_means / portfolio_stds, marker='o', cmap='viridis')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Standard Deviation (Risk)')
plt.ylabel('Expected Return')
plt.title('Efficient Frontier of Randomly Generated Portfolios')
plt.show()