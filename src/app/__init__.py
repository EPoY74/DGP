from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index() -> str:
        return "<H1> Document Generating Platform</H1>"

    return app
