class Portfolio:
    def __init__(self):
        self.stocks = []
        self.weights = []

    def add_stock(self, stock, weight):
        self.stocks.append(stock)
        self.weights.append(weight)

    def calculate_expected_return(self):
        return sum(stock.mean_return * weight for stock, weight in zip(self.stocks, self.weights))

    def calculate_variance(self):
        # This method would need to calculate the portfolio variance considering the stocks' variances and correlations.
        pass

    def calculate_sharpe_ratio(self, risk_free_rate):
        return (self.calculate_expected_return() - risk_free_rate) / self.calculate_variance()**0.5
