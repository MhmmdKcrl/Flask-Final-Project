from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_wtf.csrf import CSRFProtect


from app import app


# csrf = CSRFProtect(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
