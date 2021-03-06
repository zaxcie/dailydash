from dataclasses import dataclass

import dash_html_components as html


@dataclass
class Article:
    tile: str
    url: str
    summary: str
    source: str

    def get_dash_rep(self) -> list:
        dash_rep = list()
        dash_rep.append(html.A(html.H4(self.tile), href=self.url))
        dash_rep.append(html.P(self.summary))

        return dash_rep
