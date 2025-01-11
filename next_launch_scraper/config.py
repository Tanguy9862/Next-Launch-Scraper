from dotenv import load_dotenv
import os

env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
load_dotenv(dotenv_path=env_path)


class BaseConfig:
    SCRIPT_NAME = 'Next_Launch_Scraper'
    URL_UPCOMING_LAUNCH = 'https://nextspaceflight.com/launches/?search='
    DATA_EXPORT_FILENAME = "nsf_next_launch.json"


class LocalConfig(BaseConfig):
    DATA_DIR_NAME = 'data'


class LambdaConfig(BaseConfig):
    BUCKET_NAME = "app-space-exploration-bucket"
    DATA_EXPORT_PATH = BaseConfig.DATA_EXPORT_FILENAME


ENV = os.getenv("ENV", "local")
CONFIG = LocalConfig() if ENV == "local" else LambdaConfig()
