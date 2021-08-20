from dailydash.news.wsj import WSJArticle


def test_create_articles_from_web():
    wsj = WSJArticle.create_items()
    assert len(wsj) > 0
    assert wsj[0].source == "WSJ"
    assert all(isinstance(x, WSJArticle) for x in wsj)


def test_create_articles_from_assets():
    wsj1_path = "tests/assets/wsj1.xml"

    wsj = WSJArticle.create_items(wsj1_path)
    assert len(wsj) == 12
    assert all(isinstance(x, WSJArticle) for x in wsj)
