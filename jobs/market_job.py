from services.market_service import get_global_markets
from services.database_service import save_market_data


def update_market_data():

    from services.logger_service import logger

logger.info("Running Market Scheduler...")

    markets = get_global_markets()

    save_market_data(markets)

    logger.info("Market Data Updated Successfully")