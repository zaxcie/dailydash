import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from dailydash.news.wsj import WSJArticle

app = dash.Dash(__name__)

wsj = WSJArticle.create_articles()

app.layout = html.Div([html.H2("Wall Street Journal"),
                       html.Div(id='live-update-article'),
                      dcc.Interval(
                                    id='interval-component',
                                    interval=2000,
                                    n_intervals=0
                                )], style={"max-width": "500px"})


@app.callback(Output('live-update-article', 'children'),
              Input('interval-component', 'n_intervals'))
def update_wsj(n):
    return wsj[n % len(wsj)].get_dash_rep()


if __name__ == '__main__':
    app.run_server(debug=True)