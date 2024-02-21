import numpy as np

class CorrelationCovarianceMatrix:
    def __init__(self, stocks):
        self.stocks = stocks  # List of Stock instances
        self.correlation_matrix = np.zeros((len(stocks), len(stocks)))
        np.fill_diagonal(self.correlation_matrix, 1)  # Set diagonal to 1 for self-correlation
        self.covariance_matrix = None

    def add_correlation(self, stock1_name, stock2_name, correlation):
        if not -1 <= correlation <= 1:
            raise ValueError("Correlation must be between -1 and 1")

        index1 = self._get_stock_index(stock1_name)
        index2 = self._get_stock_index(stock2_name)

        if index1 is None or index2 is None:
            raise ValueError("Stock names must be valid")

        # Set correlation symmetrically since the matrix is symmetric
        self.correlation_matrix[index1, index2] = correlation
        self.correlation_matrix[index2, index1] = correlation

        # Invalidate the covariance matrix since we've updated correlations
        self.covariance_matrix = None

    def _get_stock_index(self, stock_name):
        for i, stock in enumerate(self.stocks):
            if stock.name == stock_name:
                return i
        return None

    def calculate_covariance_matrix(self):
        if self.covariance_matrix is not None:
            return self.covariance_matrix  # Return cached matrix if available

        std_devs = np.array([stock.std_dev for stock in self.stocks])
        std_dev_matrix = np.outer(std_devs, std_devs)
        self.covariance_matrix = std_dev_matrix * self.correlation_matrix
        return self.covariance_matrix

    def print_correlation_matrix(self):
        print("Correlation Matrix:")
        print(self.correlation_matrix)

    def print_covariance_matrix(self):
        if self.covariance_matrix is None:
            self.calculate_covariance_matrix()
        print("Covariance Matrix:")
        print(self.covariance_matrix)