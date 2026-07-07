from config import db


def save_market_data(markets):

    cursor = db.cursor()

    query = """
    INSERT INTO market_data
    (
        market_name,
        symbol,
        price,
        change_value,
        change_percent,
        market_status
    )
    VALUES
    (
        %s,%s,%s,%s,%s,%s
    )
    """

    for market in markets:

        if market["price"] is None:
            continue

        values = (
            market["name"],
            market["symbol"],
            market["price"],
            market["change"],
            market["percent"],
            market["status"]
        )

        cursor.execute(query, values)

    db.commit()

    cursor.close()