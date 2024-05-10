#run this outside flask_code folder flask --app flask_code run --debug


from flask import Flask
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import logging
import os
import importlib
import sys
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import render_template,url_for
from flaskr.config import Config
from dotenv import load_dotenv
from flask_login import LoginManager

from flask import (request, session, current_app)
from datetime import datetime
import random


db = SQLAlchemy()
# mail = Mail()
bcrypt = Bcrypt()
login_manager = LoginManager()
csrf = CSRFProtect()




load_dotenv()
# SECRET_SALT = os.getenv('SECRET_SALT')
SECRET_SALT = 'mysuperdupersecretkey'
serializer = URLSafeTimedSerializer(SECRET_SALT)


def setup_logging(app):
    logging.basicConfig(filename='blog.log', 
                    format='%(asctime)s-%(process)d-%(name)s-%(levelname)s-%(filename)s->%(funcName)s:%(lineno)s-%(message)s', 
                    level=logging.INFO, 
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    )  #basicconfig class determines name of the logging file , level, format and date stripe format
                                                  #name in format is servername
    # #serve(TransLogger(app, setup_console_handler=False))
    class IPFormatter(logging.Formatter):
        def format(self, record):
            # Add the client's IP address to the log record
            record.ip_address = request.remote_addr
            return super().format(record)
    app.logger.setLevel(logging.INFO)

# def init_db(app):
#     with app.app_context():
#         db.create_all()

# modules = [
#         {"path": "flaskr.blueprints.user",                          "name": "user"},
#         {"path": "flaskr.blueprints.auth",                          "name": "auth"},
#         {"path": "flaskr.blueprints.role",                          "name": "role"},
#         {"path": "flaskr.blueprints.profile",                       "name": "profile"},
#         {"path": "flaskr.blueprints.blog",                          "name": "blog"}
# ]


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)

    db.init_app(app)
    
    # mail.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)


    # login_manager.login_view = 'blog' #  login view defined here
    # login_manager.login_message = 'Please login to access this page!'
    # login_manager.login_message_category = 'danger'    
    login_manager.init_app(app)  # Initialize LoginManager
    setup_logging(app)
      
     
    # @app.after_request
    # def set_security_headers(response):
    #     # Prevents clickjacking
    #     response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        
    #     # Enforces HTTPS by redirecting HTTP requests
    #     response.headers['Strict-Transport-Security'] = "max-age=63072000; includeSubdomains; preload"
        
    #     # Allows serving the response to any origin
    #     # response.headers['Access-Control-Allow-Origin'] = "*"
        
    #     # Specifies the allowed headers for CORS requests
    #     # response.headers['Access-Control-Allow-Headers'] = "Content-Type, x-requested-with"
        
    #     # Prevents MIME type sniffing
    #     response.headers['X-Content-Type-Options'] = 'nosniff'
        
    #     # Controls the information sent in the Referer header
    #     response.headers['Referrer-Policy'] = 'strict-origin'
        
    #     # Sets policies for loading resources from different origins
    #     # response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    #     # response.headers['Cross-Origin-Resource-Policy'] = 'same-origin'

    #     response.headers['X-XSS-Protection'] =  "1; mode=block"
    #     # Content Security Policy (CSP) - Uncomment to enforce CSP
    #     response.headers['Content-Security-Policy'] = (
    
    #         "default-src 'self'; font-src *;img-src * data:; script-src *; style-src *;"
    #         # "script-src 'self' 'unsafe-inline';"
    #         # "object-src 'none';"
    #         # "base-uri 'none';"
    #     )
        
    #     return response
    
    
    # for module in modules:
    #     try:
    #         # print(f"registering blueprint {module['name']} from {module['path']}", end=" ")
    #         import_module = importlib.import_module(module['path'], package="flaskr")
    #         app.register_blueprint(getattr(import_module, module['name']))
    #     except Exception as e:
    #         # print("\nBlueprint not found")
    #         # print(e)
    #         sys.exit(1)
    #     # print("\t.OK")

    # @app.after_request
    # def set_session_cookie(response):
    #     response.set_cookie(
    #         'session', 
    #         value=serializer,  # Replace with your session value
    #         secure=True,  # Ensure you're using HTTPS
    #         httponly=True,  # Helps mitigate the risk of client side script accessing the protected cookie
    #         samesite='Lax'  # Allows the cookie to be sent with cross-site requests
    #     )
    #     return response
 
     # Initialize the serializer here using SECRET_SALT
   
    # Import and register blueprints
    from flaskr.blueprints.blog import blog
    app.register_blueprint(blog)
     # user_bp blueprint
    from flaskr.blueprints.auth import auth
    app.register_blueprint(auth)

    from flaskr.blueprints.role import role
    app.register_blueprint(role)
      # user_bp blueprint
    from flaskr.blueprints.profile import profile
    app.register_blueprint(profile)
    # user_bp blueprint
    from flaskr.blueprints.user import user
    app.register_blueprint(user)


    @app.route('/session/<string:user_name>')
    def set_session(user_name):
        session["user_name"] = user_name
        return f"User name {user_name} set to session"


    @app.route('/session/user')
    def get_session():
        return session["user_name"]

    
    @app.route('/test/')
    def test_page():

        return '<h1>Testing the Flask Application Factory Pattern</h1>'
    
    @app.route('/')
    def hello():
        current_datetime = datetime.now()

        # Remove milliseconds from the current datetime
        current_datetime_without_ms = current_datetime.replace(microsecond=0)
        random_number = random.randint(1, 100) 
        return f"""<h1>Hello, World!</h1>
        <h4> My random number is {random_number} </h4>
        My random number changed at {current_datetime_without_ms} 
        <p>
        To visit our blog page click 
         <a href="{url_for('blog.blog_index')}">here</a>. </p>
          <p>

        """

    with app.app_context():
        #app_name = current_app.config['APP_NAME']
        
        db.create_all()
        
        return app
