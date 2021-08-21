from dailydash.news.article import Article
import dash_html_components as html


def test_create_articles_from_assets():
    article = Article("Title", "http://test.com", "summary", "source")
    dash_rep = article.get_dash_rep()

    assert len(dash_rep) == 2
    assert isinstance(dash_rep[0], html.A)
    assert isinstance(dash_rep[0].children, html.H4)
    assert isinstance(dash_rep[1], html.P)
