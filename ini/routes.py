from flask import *

import sys 

sys.path.insert(0,'../../')

app_ = Blueprint('router',
            import_name='__name__',
            static_folder='./src',
            template_folder='./src/template'
            )

@app_.route('/',methods = ['GET'])
def index():
    return render_template('index.html')

@app_.route('/favicon.ico')
def icon_():
    return send_from_directory('C:\\Users\\USER\\OneDrive\\Documents\\Advanced Projects\\JokeX\\src\\data\\img','Icon.png')

@app_.route('/robots')
def robots():
    return send_from_directory('C:\\Users\\USER\\OneDrive\\Documents\\Advanced Projects\\JokeX\\src\\data\\docs','robots.txt')

@app_.errorhandler(404)
def _404(error):
    return render_template('404.html')