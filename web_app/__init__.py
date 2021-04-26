import os
from dotenv import load_dotenv
from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.dashboard_routes import dashboard_routes

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # set this to something else on production!!!

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.register_blueprint(home_routes)
    app.register_blueprint(dashboard_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
