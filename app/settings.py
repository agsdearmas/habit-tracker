import os
from app.services.mongo_manager.db_config import MongoConfig as dbConfig


class Config:
    SECRET_KEY = os.getenv('APP_SECRET_KEY', 'defsupersecret')
    DB_HOST = os.getenv('DB_DEFAULT_HOST', 'mongo')
    DB_PORT = os.getenv('DB_DEFAULT_PORT', '27017')
    DB_USER = os.getenv('DB_DEFAULT_USER', 'mongo_admin')
    DB_PASSWORD = os.getenv('DB_DEFAULT_PASSWORD', 'password')
    DB_NAME = os.getenv('DB_DEFAULT_NAME', 'mongo_db')

    # Lista de configuracion modular
    MONGO_DBS_ALIAS = dbConfig.MONGO_DBS_ALIAS


class DefaultConfig(Config):
    DEBUG = True


class DevelopConfig(Config):
    DEBUG = True


class StagingConfig(Config):
    DEBUG = False


class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True


class AnalyticsConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True


class TestingConfig(Config):
    TESTING = True
    MONGO_URI = 'mongodb://localhost:27017/test_habitdb'
