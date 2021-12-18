from datetime import datetime

import dash_html_components as html
import yfinance as yf


class Stock:
    def __init__(self, symbol: str):
        self.yf_ticker = yf.Ticker(symbol)
        self.yf_history_1day = self.yf_ticker.history("1d", "1m")
        self.yf_history_7days = self.yf_ticker.history("7d", "60m")
        self.yf_history_3months = self.yf_ticker.history("3mo", "1d")

        self.name = self.yf_ticker.info["shortName"]
        self.symbol = self.yf_ticker.ticker

    def _daily_open_value(self, date: str = "now"):
        _date = self._date_str_handler(date)
        open_value = self.yf_history_3months[:_date]["Open"][-1]

        return open_value

    def _lastest_close_value(self, date: str = "now"):

        _date = self._date_str_handler(date)

        subset_history_max = self.yf_history_3months[_date:_date]

        if subset_history_max.empty and not self.yf_history_7days[_date:_date].empty:
            lastest_value = self.yf_history_7days[_date:_date][-1:]["Close"][0]

        elif subset_history_max.empty:
            lastest_value = self.yf_history_3months.tail(1)["Close"][0]

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

        if daily_perf["direction"] == "Up":
            daily_color = "#00cc66"
        elif daily_perf["direction"] == "Down":
            daily_color = "#990000"
        else:
            daily_color = "#ff6600"

        dash_rep.append(html.H5(self.name + " - " + self.symbol, style={"margin-top": "0", "margin-bottom": "0"}))
        dash_rep.append(html.A(daily_change_txt, style={"color": daily_color}))

        return dash_rep

    @staticmethod
    def _date_str_handler(date: str):
        if date == "now":
            return datetime.now().strftime("%Y-%m-%d")
        else:
            return date

