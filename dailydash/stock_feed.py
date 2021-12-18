from dailydash.stock import Stock
from dailydash.feed import Feed

# WATCHLIST = ["LSPD.TO", "AAPL"]
WATCHLIST = ["LSPD.TO", "AAPL", "BMO.TO", "BNS.TO", "BTCX-B.TO", "ETHX-B.TO", "GOOG", "HXT.TO",
             "MCD", "MFC.TO", "MG", "MSFT", "VFV.TO", "VUG", "XQQ.TO", "ZCN.TO"]


class StockFeed(Feed):
    @staticmethod
    def create_items():
        stocks = list()
        for stock in WATCHLIST:
            stocks.append(Stock(stock))

        return stocks
