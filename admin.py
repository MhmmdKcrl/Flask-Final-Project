from flask_admin.contrib.sqla import ModelView

from app import admin, db

from models import Category, Product

admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))


