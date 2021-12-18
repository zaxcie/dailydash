import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

from dailydash.stock import Stock

MY_TEMPLATE = pio.templates["plotly_dark"].layout
MY_TEMPLATE.height = 300
MY_TEMPLATE.margin = {"t": 15, "r": 12}


class StockPlot:
    def __init__(self, stock: Stock):
        self.stock = stock

    def plot_daily(self):
        fig = go.Figure([go.Scatter(x=self.stock.yf_history_1day.index, y=self.stock.yf_history_1day['Open'])],
                        layout=MY_TEMPLATE)
        fig.update_layout(title=self.stock.name, margin={"t": 35, "r": 12})
        return fig

    def plot_7days(self):
        fig = go.Figure([go.Scatter(x=self.stock.yf_history_7days.index, y=self.stock.yf_history_7days['Open'])],
                        layout=MY_TEMPLATE)
        return fig

    def plot_3months(self):
        fig = go.Figure([go.Scatter(x=self.stock.yf_history_3months.index, y=self.stock.yf_history_3months['Open'])],
                        layout=MY_TEMPLATE)
        return fig
