from flask import Flask

from bookmarks.vievs import bp_main


def create_app():
    app = Flask(__name__)

    from bookmarks.vievs import bp_main
    app.register_blueprint(bp_main)

    return app
