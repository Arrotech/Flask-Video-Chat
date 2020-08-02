from flask import render_template
from app.api.v1 import video_v1

@video_v1.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')
