import plotly.graph_objects as go
import plotly.io as pio

from dailydash.stock.stock import Stock

MY_TEMPLATE = pio.templates["plotly_dark"].layout
MY_TEMPLATE.height = 280
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
        fig = self._draw_stock_plot(x=self.stock.yf_history_7days.index, y=self.stock.yf_history_7days['Open'])

        return fig

    def plot_3months(self):
        fig = self._draw_stock_plot(x=self.stock.yf_history_3months.index, y=self.stock.yf_history_3months['Open'])
        return fig

    def plot_1year(self):
        fig = self._draw_stock_plot(x=self.stock.yf_history_12months.index, y=self.stock.yf_history_12months['Open'])
        return fig

    @staticmethod
    def _draw_stock_plot(x, y):
        fig = go.Figure([go.Scatter(x=x, y=y)], layout=MY_TEMPLATE)

        fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]),  # hide weekends
                dict(values=["2015-12-25", "2016-01-01"])  # hide Christmas and New Year's
            ]
        )
        return fig
