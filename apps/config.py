# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, random, string

def get_database_uri():
    # Check if we are in production (Azure) or development
    is_production = os.getenv('FLASK_ENV', 'development') == 'production'
    
    if is_production:
        # Production: Use Azure Postgres
        DB_ENGINE = 'postgresql'
        DB_USERNAME = os.getenv('DB_USERNAME', 'southerninterests_webapp')
        DB_PASS = os.getenv('DB_PASS', '600Bonaventure!')
        DB_HOST = os.getenv('DB_HOST', 'southern-interests-db.postgres.database.azure.com')
        DB_PORT = os.getenv('DB_PORT', '5432')
        DB_NAME = os.getenv('DB_NAME', 'postgres')
        
        return f'{DB_ENGINE}://{DB_USERNAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    else:
        # Development: Use SQLite
        basedir = os.path.abspath(os.path.dirname(__file__))
        return f'sqlite:///{os.path.join(basedir, "app.db")}'

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')  
    
    # Set up the App SECRET_KEY
    SECRET_KEY  = os.getenv('SECRET_KEY', None)
    if not SECRET_KEY:
        SECRET_KEY = ''.join(random.choice(string.ascii_lowercase) for i in range(32))     

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = get_database_uri()

class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}

