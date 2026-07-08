from flask import Flask, render_template
from config import db
from services.market_service import get_global_markets
from services.database_service import save_market_data
from services.scheduler_service import start_scheduler

app = Flask(__name__)

start_scheduler()


@app.route("/")
def dashboard():

    status = "Connected" if db.is_connected() else "Disconnected"

    markets = get_global_markets()

    return render_template(
        "dashboard.html",
        db_status=status,
        markets=markets
    )


if __name__ == "__main__":
    app.run(debug=True)