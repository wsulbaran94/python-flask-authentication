import os

# Get the database configuration from environment variables
DATABASE_CONFIG = os.getenv('DB_CONFIGURATION', default='SQLite')

class MySQLConfig:
  SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_DATABASE_URI', default='mysql+mysqlconnector://username:password@localhost/dbname')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class SQLiteConfig:
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLITE_DATABASE_URI', default='sqlite:///db.sqlite')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class DataBaseConfiguration:
  if DATABASE_CONFIG == 'MYSQL':
    db = MySQLConfig
  else:
    db = SQLiteConfig

class DevelopmentConfig(DataBaseConfiguration.db):
  DEBUG = True

config = {
  'development': DevelopmentConfig
}