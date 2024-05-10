import os
from dotenv import load_dotenv


load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://sql_blog2:Ejn9$b484@socodb:3306/db_blog2'
    SECRET_KEY = 'ciaotutttttttttttti'
    # SECRET_KEY = os.getenv("SECRET_KEY")
#     SCHEMA_NAME = os.environ.get("SCHEMA_NAME")
#     DBHOST = os.environ.get("DBHOST")
#     PW = os.environ.get("PW")
#     DBUSER = os.environ.get("DBUSER")

#     SQLALCHEMY_DATABASE_URI = (
#         f"mysql+pymysql://{DBUSER}:{PW}@{DBHOST}/{SCHEMA_NAME}?charset=utf8mb4"
#     )
    # SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get
    # SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE")
    # MAIL_SERVER = "twces01.twra.tomware.it"
    # MAIL_PORT = 25
    # MAIL_USERNAME = None
    # MAIL_PASSWORD = None
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = False
    # MAIL_DEFAULT_SENDER = "noreply@tomware.it"
    # MAIL_MAX_EMAILS = os.environ.get("MAIL_MAX_EMAILS")
    # MAIL_SUPPRESS_SEND = os.environ.get("MAIL_SUPPRESS_SEND")
    # MAIL_ASCII_ATTACHMENTS = os.environ.get("MAIL_ASCII_ATTACHMENTS")
    # SECRET_KEY = "thisisasecretkey"
    # SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT")
    # LOG_TYPE = os.environ.get("LOG_TYPE", "watched")
    # LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    # # File Logging Setup
    # LOG_DIR = os.environ.get("LOG_DIR", "./")
    # APP_LOG_NAME = os.environ.get("APP_LOG_NAME", "app.log")
    # WWW_LOG_NAME = os.environ.get("WWW_LOG_NAME")

    # Configure cookie settings
