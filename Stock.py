class Stock:
    def __init__(self, name, mean_return, std_dev, correlations=None):
        self.name = name
        self.mean_return = mean_return
        self.std_dev = std_dev
        self.correlations = correlations or {}
        
    def add_correlation(self, other_stock, correlation):
        self.correlations[other_stock.name] = correlation
        other_stock.correlations[self.name] = correlation