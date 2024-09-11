from flask import Flask

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345@localhost:3306/new_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin


db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app, name = "E-commerce", template_mode='bootstrap3')


from controllers import *
from models import *
# from extensions import *

if __name__ == '__main__':
    from admin import *
    app.run(debug=True)