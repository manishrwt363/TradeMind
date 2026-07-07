import yfinance as yf


MARKETS = {
    "Dow Jones": "^DJI",
    "Nasdaq": "^IXIC",
    "S&P 500": "^GSPC",
    "Gold": "GC=F",
    "Crude Oil": "CL=F",
    "USD/INR": "INR=X"
}


def get_global_markets():

    result = []

    for name, symbol in MARKETS.items():

        try:
            ticker = yf.Ticker(symbol)
            info = ticker.fast_info

            current = round(info.get("lastPrice", 0), 2)
            previous = round(info.get("previousClose", current), 2)

            change = round(current - previous, 2)

            if previous != 0:
                percent = round((change / previous) * 100, 2)
            else:
                percent = 0

            status = "Bullish" if change >= 0 else "Bearish"

            result.append({
                "name": name,
                "symbol": symbol,
                "price": current,
                "change": change,
                "percent": percent,
                "status": status
            })

        except Exception as e:

            result.append({
                "name": name,
                "symbol": symbol,
                "price": None,
                "change": None,
                "percent": None,
                "status": "Unavailable"
            })

    return result