from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path.cwd() / ".env"
load_dotenv(dotenv_path=env_path)
ENV = os.getenv("ENV", "local")


# Only for if you want to access to your Cloud Storage from Local
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'spacexploration-gcp-bucket-access.json' or None


class BaseConfig:
    SCRIPT_NAME = 'nsf_next_launch_scraper'
    URL_UPCOMING_LAUNCH = 'https://nextspaceflight.com/launches/?search='
    DATA_EXPORT_FILENAME = "nsf_next_launch.json"


class LocalConfig(BaseConfig):
    DATA_DIR_NAME = 'data'


class AWSConfig(BaseConfig):
    BUCKET_NAME = "app-space-exploration-bucket"


class GCPConfig(BaseConfig):
    BUCKET_NAME = 'space-exploration-bucket-test'


def get_config():
    if ENV == "local":
        return LocalConfig()
    elif ENV == 'aws':
        return AWSConfig()
    elif ENV == 'gcp':
        return GCPConfig()
    return LocalConfig()


CONFIG = get_config()
