from dataclasses import dataclass

from dash import html


@dataclass
class Article:
    tile: str
    url: str
    summary: str
    source: str

    def get_dash_rep(self):
        dash_rep = html.A(self.tile, href=self.url)
        # dash_rep.append(html.P(self.summary))

        return dash_rep
