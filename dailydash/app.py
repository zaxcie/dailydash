import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from dailydash.news.wsj import WSJArticle
from dailydash.news.mw import MWArticle
from dailydash.stock import Stock
from dailydash.stock_plot import StockPlot
from dailydash.stock_feed import StockFeed
from dailydash.stocks_performance import StocksPerformance

app = dash.Dash(__name__)

wsj = WSJArticle.create_items()
mw = MWArticle.create_items()
print("Loaded articles")

stocks = StockFeed.create_items()
daily_perf_stocks = StocksPerformance(stocks)
print("Loaded fin data")

app.layout = html.Div([html.Div([html.H2("Wall Street Journal"),
                                 html.Div(id='live-update-wsj', style={"max-height": "360px"}),
                                 dcc.Interval(
                                     id='interval-component-wsj',
                                     interval=20000,
                                     n_intervals=0
                                 ),
                                 html.H2("MarketWatch"),
                                 html.Div(id='live-update-mw', style={"max-height": "360px"}),
                                 dcc.Interval(
                                     id='interval-component-mw',
                                     interval=20000,
                                     n_intervals=0
                                 )
                                 ], style={"max-width": "500px",
                                           "float": "left"}),
                       html.Div([
                                 html.H2("Financial Graph"),
                                 html.Div(id='live-update-daily', style={"max-height": "260px"}),
                                 dcc.Interval(
                                     id='interval-component-dailyplot',
                                     interval=20000,
                                     n_intervals=0
                                 ),
                                 html.Div(id='live-update-7days', style={"max-height": "260px"}),
                                 dcc.Interval(
                                     id='interval-component-7daysplot',
                                     interval=20000,
                                     n_intervals=0
                                 ),
                                 html.Div(id='live-update-3months', style={"max-height": "260px"}),
                                 dcc.Interval(
                                     id='interval-component-3monthsplot',
                                     interval=20000,
                                     n_intervals=0
                                 )
                                 ], style={"max-width": "1100px",
                                           "min-width": "1100px",
                                           "float": "left"}),

                       html.Div([
                                 html.H2("Daily performance"),
                                 html.Div(id='live-update-daily-performance'),
                                 dcc.Interval(
                                     id='interval-component-daily-performance',
                                     interval=200000,
                                     n_intervals=0
                                 )
                                 ], style={"max-width": "450px",
                                           "min-width": "450px",
                                           "margin-left": "1400px"})
                       ])


# TODO investigate to see if this can move somewhere else
@app.callback(Output('live-update-wsj', 'children'),
              Input('interval-component-wsj', 'n_intervals'))
def update_wsj(n):
    return wsj[n % len(wsj)].get_dash_rep()


@app.callback(Output('live-update-mw', 'children'),
              Input('interval-component-mw', 'n_intervals'))
def update_mw(n):
    return mw[n % len(mw)].get_dash_rep()


@app.callback(Output('live-update-feedly', 'children'),
              Input('interval-component-feedly', 'n_intervals'))
def update_feedly(n):
    return mw[n % len(mw)].get_dash_rep()  # TODO change feedly to actually be feedly


@app.callback(Output('live-update-daily', 'children'),
              Input('interval-component-dailyplot', 'n_intervals'))
def update_fingraph_daily(n):
    stock_plot = StockPlot(stocks[n % len(stocks)])
    return dcc.Graph(
        id='daily',
        figure=stock_plot.plot_daily()
    )


@app.callback(Output('live-update-7days', 'children'),
              Input('interval-component-7daysplot', 'n_intervals'))
def update_fingraph_7days(n):
    stock_plot = StockPlot(stocks[n % len(stocks)])
    return dcc.Graph(
        id='7days',
        figure=stock_plot.plot_7days()
    )


@app.callback(Output('live-update-3months', 'children'),
              Input('interval-component-3monthsplot', 'n_intervals'))
def update_fingraph_3months(n):
    stock_plot = StockPlot(stocks[n % len(stocks)])
    return dcc.Graph(
        id='3months',
        figure=stock_plot.plot_3months()
    )


@app.callback(Output('live-update-daily-performance', 'children'),
              Input('interval-component-daily-performance', 'n_intervals'))
def update_daily_perf(n):
    return daily_perf_stocks.get_dash_rep()


if __name__ == '__main__':
    app.run_server(debug=False)
