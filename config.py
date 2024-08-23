import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


class Config:
    # SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
