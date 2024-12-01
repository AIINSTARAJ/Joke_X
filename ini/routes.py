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
    return f'JOKEMOJI'

@app_.route('/favicon.ico')
def icon_():
    return send_from_directory('C:\\Users\\USER\\OneDrive\\Documents\\Advanced Projects\\JokeX\\src\\data\\img','Icon.ico')

