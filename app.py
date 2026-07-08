from flask import Flask

from services.scheduler_service import start_scheduler

from routes.dashboard import dashboard_bp

from routes.api import api_bp

app = Flask(__name__)

app.register_blueprint(dashboard_bp)

app.register_blueprint(api_bp)

start_scheduler()

if __name__ == "__main__":
    app.run(debug=True)