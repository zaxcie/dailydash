import feedparser

from dailydash.news.article import Article

WSJ_RSS_URL = 'https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml'


class WSJArticle(Article):
    def __init__(self, parser_entry):
        super().__init__(parser_entry.title, parser_entry.link, parser_entry.summary, "WSJ")

    @staticmethod
    def create_articles(url_rss_feed=WSJ_RSS_URL):
        parser = feedparser.parse(url_rss_feed)
        articles = list()

        for entry in parser.entries:
            articles.append(WSJArticle(entry))

        return articles
