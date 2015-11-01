from flask import *
import os
import os.path

app = Flask(__name__)

@app.route('/bower/<path:path>')
def bower(path):
    return send_file(os.path.join(os.path.dirname(os.getcwd()), 'bower_components', path))

@app.route('/')
def index():
    return render_template('index.html')
