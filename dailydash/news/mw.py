import feedparser

from dash import html

from dailydash.news.article import Article
from dailydash.feed import Feed

MW_RSS_URL = 'http://feeds.marketwatch.com/marketwatch/marketpulse/'


class MWArticle(Article, Feed):
    def __init__(self, parser_entry):
        super().__init__(parser_entry.title, parser_entry.link, parser_entry.summary, "MW")

    @staticmethod
    def create_items(url_rss_feed=MW_RSS_URL):
        parser = feedparser.parse(url_rss_feed)
        articles = list()

        for entry in parser.entries:
            entry.summary = MWArticle._clean_summary(entry.summary)
            articles.append(MWArticle(entry).get_dash_rep())
            articles.append(html.Br())

        return articles

    @staticmethod
    def _clean_summary(text):
        cleaned_text = text.split("</p>")[0]
        cleaned_text = cleaned_text.replace("<p>", "")
        cleaned_text = cleaned_text.replace("&amp;", "&")

        return cleaned_text
