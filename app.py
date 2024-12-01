from flask import *


app = Flask(__name__,
            static_folder='src',
            template_folder='src/template'
            )

from ini.routes import app_

from ini.data import *

app.config.from_pyfile('ini\\cfg.py')

db.init_app(app)

app.register_blueprint(app_)


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=6225,
        debug = app.config['DEBUG']
    )