from flask import Blueprint, jsonify

from services.database_service import get_market_history

api_bp = Blueprint("api", __name__)


@api_bp.route("/api/history/<symbol>")
def market_history(symbol):

    history = get_market_history(symbol)

    return jsonify(history)