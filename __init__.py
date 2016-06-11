from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB':"my_tumble_log"}
app.config["SECRET_KEY"] = "KSFSDFSDFSGKSDJFGKDFGJDFGJDFKGDFJGDFKGJDFKGJ"

db = MongoEngine(app)


if __name__ == '__main__':
    app.run()
    
def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    app.register_blueprint(posts)

register_blueprints(app)