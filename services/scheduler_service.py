from apscheduler.schedulers.background import BackgroundScheduler

from jobs.market_job import update_market_data


scheduler = BackgroundScheduler()


def start_scheduler():

    scheduler.add_job(
        update_market_data,
        trigger="interval",
        minutes=5
    )

    scheduler.start()

    from services.logger_service import logger

logger.info("Scheduler Started")