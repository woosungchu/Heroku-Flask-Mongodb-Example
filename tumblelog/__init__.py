from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

db = MongoEngine(app)


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
    
def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    app.register_blueprint(posts)

register_blueprints(app)