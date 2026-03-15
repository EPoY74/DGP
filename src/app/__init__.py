from flask import Flask

from app.routes import (
    documents_bp,
    main_bp,
)


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(main_bp)
    app.register_blueprint(documents_bp)

    return app
