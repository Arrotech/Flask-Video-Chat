import os
from app import video_app

config_name = os.getenv('FLASK_ENV')
app = video_app(config_name)

if __name__ == '__main__':
    app.run()