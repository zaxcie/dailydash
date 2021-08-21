import numpy as np

from dailydash.stock import Stock


def test_daily_open_value():
    ticker_symbol = "msft"

    msft = Stock(ticker_symbol)
    np.testing.assert_almost_equal(msft._daily_open_value("2021-08-20"), 299.72000, 5)


def test_lastest_close_value():
    ticker_symbol = "msft"
    msft = Stock(ticker_symbol)
    latest_value = msft._lastest_close_value("2021-08-20")

    np.testing.assert_almost_equal(latest_value, 304.35999, 5)


def test_daily_performance():
    ticker_symbol = "msft"
    msft = Stock(ticker_symbol)

    # 1.548%
    assert msft.daily_performance("2021-08-20")["direction"] == "Up"
    np.testing.assert_almost_equal(msft.daily_performance("2021-08-20")["raw"], 4.63999, 2)
    np.testing.assert_almost_equal(msft.daily_performance("2021-08-20")["percent"], 1.548, 2)


def test_date_handler():
    Stock._date_str_handler("now")