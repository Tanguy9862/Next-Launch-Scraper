from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path.cwd() / ".env"
load_dotenv(dotenv_path=env_path)


class BaseConfig:
    SCRIPT_NAME = 'nsf_next_launch_scraper'
    URL_UPCOMING_LAUNCH = 'https://nextspaceflight.com/launches/?search='
    DATA_EXPORT_FILENAME = "nsf_next_launch.json"


class LocalConfig(BaseConfig):
    DATA_DIR_NAME = 'data'


class LambdaConfig(BaseConfig):
    BUCKET_NAME = "app-space-exploration-bucket"


ENV = os.getenv("ENV", "local")
CONFIG = LocalConfig() if ENV == "local" else LambdaConfig()
