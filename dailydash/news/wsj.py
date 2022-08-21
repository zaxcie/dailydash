import feedparser

from dash import html

from dailydash.news.article import Article
from dailydash.feed import Feed

WSJ_RSS_URL = 'https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml'


class WSJArticle(Article, Feed):
    def __init__(self, parser_entry):
        super().__init__(parser_entry.title, parser_entry.link, parser_entry.summary, "WSJ")

    @staticmethod
    def create_items(url_rss_feed=WSJ_RSS_URL):
        parser = feedparser.parse(url_rss_feed)
        articles = list()

        for entry in parser.entries:
            articles.append(WSJArticle(entry).get_dash_rep())
            articles.append(html.Br())

        return articles
