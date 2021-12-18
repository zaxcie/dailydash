import itertools


class StocksPerformance:
    def __init__(self, stocks):
        self.stocks = stocks

    def get_dash_rep(self):
        dash_rep = list()
        for stock in self.stocks:
            dash_rep.append(stock.get_daily_performance_dash_rep())

        dash_rep = list(itertools.chain(*dash_rep))

        return dash_rep

# Market Cap, P/E,