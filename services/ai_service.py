MARKET_WEIGHTS = {

    "S&P 500":30,

    "Nasdaq":25,

    "Dow Jones":20,

    "Crude Oil":10,

    "Gold":10,

    "USD/INR":5

}

def generate_market_analysis(markets):

    bullish = 0
    bearish = 0

    highlights = []

    for market in markets:

        percent = market["change_percent"]
        name = market["name"]

        if percent >= 0:

            weight = MARKET_WEIGHTS.get(name,5)

            bullish += weight
            highlights.append(f"{name} gained {percent}%")

        else:

            weight = MARKET_WEIGHTS.get(name,5)

            bearish += weight
            highlights.append(f"{name} fell {abs(percent)}%")

    if bullish > bearish:

        sentiment = "Bullish"

        total = bullish + bearish

        confidence = round((bullish / total) * 100)

        summary = (
            "Global markets are showing positive momentum. "
            "Investors are displaying healthy risk appetite."
        )

    elif bearish > bullish:

        sentiment = "Bearish"

        total = bullish + bearish

        confidence = round((bearish / total) * 100)

        summary = (
            "Selling pressure dominates global markets. "
            "Investors appear to be risk-averse."
        )

    else:

        sentiment = "Neutral"

        confidence = 50

        summary = (
            "Markets are mixed with no clear direction."
        )

    return {

        "sentiment": sentiment,

        "confidence": confidence,

        "summary": summary,

        "highlights": highlights

    }