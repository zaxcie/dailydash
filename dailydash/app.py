import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from dailydash.news.wsj import WSJArticle
from dailydash.news.mw import MWArticle
from dailydash.stock import Stock

app = dash.Dash(__name__)

wsj = WSJArticle.create_items()
mw = MWArticle.create_items()

msft = Stock("msft")
ifc_to = Stock("ifc.to")

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
                                 ),
                                 html.H2("Feedly"),
                                 html.Div(id='live-update-feedly', style={"max-height": "360px"}),
                                 dcc.Interval(
                                     id='interval-component-feedly',
                                     interval=20000,
                                     n_intervals=0
                                 )
                                 ], style={"max-width": "500px",
                                           "float": "left"}),
                       html.Div([
                                 html.H2("Daily performance"),
                                 html.Div(id='live-update-msft'),
                                 dcc.Interval(
                                     id='interval-component-msft',
                                     interval=200000,
                                     n_intervals=0
                                 ),
                                 html.Div(id='live-update-ifc_to'),
                                 dcc.Interval(
                                     id='interval-component-ifc_to',
                                     interval=200000,
                                     n_intervals=0
                                 )
                                 ], style={"max-width": "300px",
                                           "margin-left": "15px",
                                           "float": "left"})
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
    return mw[n % len(mw)].get_dash_rep()


@app.callback(Output('live-update-msft', 'children'),
              Input('interval-component-msft', 'n_intervals'))
def update_msft(n):
    return msft.get_daily_performance_dash_rep()


@app.callback(Output('live-update-ifc_to', 'children'),
              Input('interval-component-ifc_to', 'n_intervals'))
def update_ifc_to(n):
    return ifc_to.get_daily_performance_dash_rep()


if __name__ == '__main__':
    app.run_server(debug=True)
