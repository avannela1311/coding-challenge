from flask import Flask
from common.config import DevelopmentConfig, TestingConfig, ProductionConfig
import os
from routes.invitation_routes import invitation_bp

# Initialize Flask app
app = Flask(__name__)

# Load configuration based on environment variable
if os.getenv('FLASK_DEBUG') == 'development':
    app.config.from_object(DevelopmentConfig)
elif os.getenv('FLASK_DEBUG') == 'testing':
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(ProductionConfig)

# Register routes blueprint
app.register_blueprint(invitation_bp)

if __name__ == "__main__":
    app.run(debug=True)

#
# Explanation:
#
# Flask app initialization (app = Flask(__name__)): Initializes the Flask app object. The __name__ argument helps Flask identify where the application is located.
# Loading configuration (app.config.from_object(Config)): Loads configuration settings from a Config class defined in config.py. This will help us keep environment-specific variables.
# Registering Blueprints (app.register_blueprint(invitation_bp)): Blueprints allow us to organize the app’s routes. Here, we register the invitation_bp blueprint, which handles invitation generation routes.
# Logging setup (logging.basicConfig(level=logging.INFO)): Configures logging for the app, setting the log level to INFO for detailed logs.
# App run (app.run(debug=True)): Runs the Flask app in debug mode, enabling auto-reloading and detailed error messages for development.
