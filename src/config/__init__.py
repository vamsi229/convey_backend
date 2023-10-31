import configparser
import os
from dotenv import load_dotenv

config = configparser.ConfigParser()
config.read("conf/application.conf")
load_dotenv(dotenv_path=".env")


class SERVICE_DETAILS:
    HOST = os.getenv("host", config.get('SERVICE', 'host'))
    PORT = os.getenv("port", config.get('SERVICE', 'port'))


class MONGO:
    MONGO_DATABASE = os.getenv('DATABASE', config.get('MONGO_DB', "database"))
    MONGO_URI = os.getenv('MONGO_URI', config.get('MONGO_DB', "mongo_uri"))