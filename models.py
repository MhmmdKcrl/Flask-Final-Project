from app import db



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    parent = db.relationship('Category', remote_side=[id], backref=db.backref('children', uselist=True, cascade='delete,all'))

    def __repr__(self):
        return f'Category {self.title}'


class ProductImages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('images', uselist=True, cascade='delete,all'))

    image = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'ProductImages {self.id}'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.Text, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('products', uselist=True, cascade='delete,all'))

    def __repr__(self):
        return f'Product {self.name}'