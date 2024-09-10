from flask import Flask, render_template, request, redirect, url_for, flash, session


from app import app
from models import Category, Product


@app.route('/')
def index():
    products = Product.query.all()
    categories = Category.query.all()

    cat_ids =  request.args.get('cat')
    if cat_ids:
        products = []
        cat_ids = cat_ids.split(',')

        for i in categories:
            categories = Category.query.filter_by(parent_id=i.id).all()
            product = Product.query.filter_by(category_id=i.id).all()
            products.extend(product)
            i.count = len(product)
            if i.children:
                for j in i.children:
                    product = Product.query.filter_by(category_id=j.id).all()
                    products.extend(product)
                i.count = len(products)
        

                
        
    context = {
        'products': products,
        'categories': categories
    }
    return render_template('shop.html', **context)


