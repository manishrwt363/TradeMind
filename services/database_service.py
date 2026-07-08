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


def get_latest_market_data():

    cursor = db.cursor(dictionary=True)

    query = """
    SELECT

        m1.market_name AS name,
        m1.symbol,
        m1.price,
        m1.change_value AS change_value,
        m1.change_percent AS change_percent,
        m1.market_status AS market_status,
        m1.fetch_time
    FROM market_data m1
    INNER JOIN
    (
        SELECT
            symbol,
            MAX(fetch_time) latest_time
        FROM market_data
        GROUP BY symbol
    ) m2
        ON m1.symbol = m2.symbol
       AND m1.fetch_time = m2.latest_time
    ORDER BY m1.market_name;
    """
    
    print(query)
    cursor.execute(query)

    data = cursor.fetchall()

    for row in data:

        row["fetch_time"] = row["fetch_time"].strftime("%I:%M %p")

    cursor.close()
    
    return data


def get_market_statistics():

    cursor = db.cursor(dictionary=True)

    query = """
    SELECT

        market_name,

        ROUND(MAX(price),2) AS highest_price,

        ROUND(MIN(price),2) AS lowest_price,

        ROUND(AVG(price),2) AS average_price,

        COUNT(*) AS total_records

    FROM market_data

    GROUP BY market_name

    ORDER BY market_name;
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()

    return data