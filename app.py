from flask import Flask, render_template
from config import db
from services.market_service import get_global_markets
from services.database_service import save_market_data
from services.scheduler_service import start_scheduler
from services.database_service import get_latest_market_data
from services.database_service import get_market_statistics

app = Flask(__name__)

start_scheduler()


@app.route("/")

def dashboard():

    status = "Connected" if db.is_connected() else "Disconnected"

    markets = get_latest_market_data()

    statistics = get_market_statistics()

    return render_template(
        "dashboard.html",
        db_status=status,
        markets=markets,
        statistics=statistics
    )


if __name__ == "__main__":
    app.run(debug=True)