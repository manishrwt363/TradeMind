from flask import Blueprint, render_template

from config import db

from services.database_service import (
    get_latest_market_data,
    get_market_statistics
)

from services.ai_service import generate_market_analysis

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def dashboard():

    status = "Connected" if db.is_connected() else "Disconnected"

    markets = get_latest_market_data()

    statistics = get_market_statistics()

    analysis = generate_market_analysis(markets)

    return render_template(
        "dashboard.html",
        db_status=status,
        markets=markets,
        statistics=statistics,
        analysis=analysis
    )