from dailydash.news.wsj import WSJArticle


def test_create_articles_from_web():
    wsj = WSJArticle.create_articles()
    assert len(wsj) > 0
    assert all(isinstance(x, WSJArticle) for x in wsj)


def test_create_articles_from_assets():
    wsj1_path = "tests/assets/wsj1.xml"

    wsj = WSJArticle.create_articles(wsj1_path)
    assert len(wsj) == 12
    assert all(isinstance(x, WSJArticle) for x in wsj)
