import os
from os import path
from dotenv import load_dotenv
from flask import Flask
from app.config import app_config
from app.api.v1 import video_v1

def video_app(config_name):
    
    app = Flask(__name__, template_folder='../../../templates')
    
    config_name = os.getenv('FLASK_ENV')
    app.config.from_pyfile('config.py')
    app.config['SECRET_KEY'] = "videochat"
    
    app.register_blueprint(video_v1, url_prefix='/api/v1/')
        
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, '.env'))

    return app