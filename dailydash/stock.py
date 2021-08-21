from datetime import datetime

import dash_html_components as html
import yfinance as yf


class Stock:
    def __init__(self, symbol: str):
        self.yf_ticker = yf.Ticker(symbol)
        self.yf_history_max = self.yf_ticker.history("max")
        self.yf_history_7days = self.yf_ticker.history("7d", "1m")

        self.name = self.yf_ticker.info["shortName"]
        self.symbol = self.yf_ticker.ticker

    def _daily_open_value(self, date: str = "now"):
        _date = self._date_str_handler(date)
        open_value = self.yf_history_max[:_date]["Open"][-1]

        return open_value

    def _lastest_close_value(self, date: str = "now"):

        _date = self._date_str_handler(date)

        subset_history_max = self.yf_history_max[_date:_date]

        if subset_history_max.empty and not self.yf_history_7days[_date:_date].empty:
            lastest_value = self.yf_history_7days[_date:_date][-1:]["Close"][0]

        elif subset_history_max.empty:
            lastest_value = self.yf_history_max.tail(1)["Close"][0]

        else:
            lastest_value = subset_history_max[-1:]["Close"][0]

        return lastest_value

    def daily_performance(self, date: str = "now"):
        _date = self._date_str_handler(date)

        open_value = self._daily_open_value(_date)
        last_value = self._lastest_close_value(_date)

        raw = round(last_value - open_value, 2)
        percent = round((raw / open_value) * 100, 2)
        if raw > 0.009:
            direction = "Up"
        elif raw < -0.009:
            direction = "Down"
        else:
            direction = "Neutral"

        daily_perf = {"raw": raw,
                      "percent": percent,
                      "direction": direction}

        return daily_perf

    def get_daily_performance_dash_rep(self) -> list:
        dash_rep = list()
        # Company name, Symbol
        # Today % change, raw value
        daily_perf = self.daily_performance()
        daily_change_txt = '{raw} ({percent}%)'.format(raw=daily_perf["raw"], percent=daily_perf["percent"])

        dash_rep.append(html.H4(self.name))
        dash_rep.append(html.H6(self.symbol))
        dash_rep.append(html.A(daily_change_txt))

        return dash_rep

    @staticmethod
    def _date_str_handler(date: str):
        if date == "now":
            return datetime.now().strftime("%Y-%m-%d")
        else:
            return date

