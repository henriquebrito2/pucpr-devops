from api import Api
from flask import Flask


def main():
    # Creates the Flask app
    app = Flask(__name__)
    
    # Instantiates the Example class and registers its blueprints
    api = Api()
    app.register_blueprint(api.blueprint)
    
    # Runs the app
    app.run()

if __name__ == '__main__':
    main()
