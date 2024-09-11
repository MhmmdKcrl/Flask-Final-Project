from flask import Flask, render_template, request, redirect, url_for

from app import app

from models import Category, Product


@app.route('/')
def shop():
    categories = Category.query.all()
    products = Product.query.all()

    for i in products:
        print(i.image)

    cat = request.args.get('category')
    if cat:
        cat_list = cat.split(',')
        cat_list = [int(i) for i in cat_list]
        products = []
        for i in cat_list:
            products += Product.query.filter_by(category_id=i).all()

        # products = Product.query.filter(Product.category_id.in_(cat_list)).all()

    context = {
        'categories': categories,
        'products': products
    }
    return render_template('shop.html', **context)

