import os


class Config:
    DEBUG = False
    SECRET_KEY = "EZK5UYPLkiYfGEE8wPVR8Z28zWeBSZtG"


class ProdConfig(Config):
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")


class DevConfig(Config):
    DEBUG = True


def apply_config(app):
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProdConfig")
    else:
        app.config.from_object("config.DevConfig")
    print(f"App is running with ENV={app.config['ENV']}")
