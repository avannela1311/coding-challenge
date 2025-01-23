import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    """Base configuration class."""
    ENV = os.getenv("FLASK_DEBUG", "production")  # Default to production if not set
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
    DEBUG = False
    TESTING = False
    LOGGING_LEVEL = "INFO"
    PARTNER_API_URL = os.getenv("PARTNER_API_URL", "https://api.example.com/partners")
    INVITATION_API_URL = os.getenv("INVITATION_API_URL", "https://api.example.com/invitation")
    DATE_FORMAT = "%Y-%m-%d"
    DIFF_IN_DAYS = 1

class DevelopmentConfig(Config):
    """Configuration for the development environment."""
    DEBUG = True
    LOGGING_LEVEL = "DEBUG"
    PARTNER_API_URL = "https://dev-api.example.com/partners"
    INVITATION_API_URL = "https://dev-api.example.com/invitation"


class TestingConfig(Config):
    """Configuration for testing environment."""
    TESTING = True
    LOGGING_LEVEL = "ERROR"
    PARTNER_API_URL = "https://test-api.example.com/partners"
    INVITATION_API_URL = "https://test-api.example.com/invitation"


class ProductionConfig(Config):
    """Configuration for the production environment."""
    DEBUG = False
    LOGGING_LEVEL = "INFO"
    PARTNER_API_URL = os.getenv("PROD_PARTNER_API_URL")
    INVITATION_API_URL = os.getenv("PROD_INVITATION_API_URL")

#
# Explanation:
#
# Config class: This class holds all the configuration variables for the app. These are accessed globally throughout the app via app.config.
# DEBUG = True: This enables Flask’s debug mode, which provides more detailed error messages and auto-reloads the server during development.
# SECRET_KEY: This is used for securely signing cookies and sessions. In a production app, it should be a randomly generated secret key.
# URLs (PARTNER_SERVICE_URL, INVITATION_SERVICE_URL): These are example URLs for external services that the app may interact with. You can configure actual URLs based on your environment.