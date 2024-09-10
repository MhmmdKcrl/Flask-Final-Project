from flask import Flask 


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345@localhost:3306/test_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# app.config['SECRET_KEY'] = '5307af8b5240a5366c9cf3cc3c838c7fe9893f1a9e1227609091ded7e8593f46'

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_wtf.csrf import CSRFProtect

# csrf = CSRFProtect(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers import *
from models import *

if __name__ == '__main__':
    
    app.run(debug=True)

