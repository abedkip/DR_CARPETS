from app import app, db
from flask import render_template, session
from app.models import CartItem  # Import the CartItem model


@app.route('/')
def Home():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

# COLORS DROPDOWN
@app.route('/color/black')
def black():
    return render_template('black.html')

@app.route('/color/blue')
def blue():
    return render_template('blue.html')

@app.route('/color/grey')
def grey():
    return render_template('grey.html')

@app.route('/color/red')
def red():
    return render_template('red.html')

# CARPETS STYLES DROPDOWN
@app.route('/Classic Carpets')
def classic_carpets():
    return render_template('classic_carpets.html')

@app.route('/Modern Carpets')
def modern_carpets():
    return render_template('modern_carpets.html')

@app.route('/Turkish Carpets')
def turkish_carpets():
    return render_template('turkish_carpets.html')

# CARPET SIZES DROPDOWN

@app.route('/4ft x 6ft')
def ft_4x6():
    return render_template('4ft_6ft.html')


@app.route('/5ft x 8ft')
def ft_5x8():
    return render_template('5ft_8ft.html')

@app.route('/6ft x 9ft')
def ft_6x9():
    return render_template('6ft_9ft.html')

@app.route('/7ft x 10ft')
def ft_7x10():
    return render_template('7ft_10ft.html')

# faq route
@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

# DR_DEALS ROUTE
@app.route('/deals')
def dr_deals():
    products = [
        {
            "name": "Alin Abstract Carpet",
            "image": "/static/images/image1.jpg",
            "old_price": "11,929.00",
            "name": "8,049.00",
            "sold_out": True,
            "url": "#"
        },
        {
              "name": "Alin Beige Dream Carpet",
            "image": "/static/images/image2.jpg",
            "old_price": "11,929.00",
            "name": "8,049.00",
            "sold_out": True,
            "url": "#"
        },
          {
            "name": "Alin Abstract Carpet",
            "image": "/static/images/image3.jpg",
            "old_price": "11,929.00",
            "name": "8,049.00",
            "sold_out": True,
            "url": "#"
        },
        {
              "name": "Alin Beige Dream Carpet",
            "image": "/static/images/image4.jpg",
            "old_price": "11,929.00",
            "name": "8,049.00",
            "sold_out": True,
            "url": "#"
        },
          {
            "name": "Alin Abstract Glow Carpet",
            "image": "/static/images/image1.jpg",
            "old_price": "11,929.00",
            "name": "8,049.00",
            "sold_out": True,
            "url": "#"
        },
        {
            "name": "Alin Beige Dream Gold Carpet",
            "image": "/static/images/image4.jpg",
            "old_price": "11,929.00",
            "name": "8,049.00",
            "sold_out": True,
            "url": "#"
        }
        
        
        
        
        
           ]
    
    colors = ["A.Bej/A.Bej", "A.Gri/A.Gri", "A.Gri/A.Mavi", "A.Gri/Beyaz"]
    
    return render_template("dr_deals.html", products=products, colors=colors)



# REGISTRATION ROUTE



























# Add item to cart
def add_to_basket(product_id, quantity):
    cart = session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + quantity
    session['cart'] = cart

# Get cart
def get_cart():
    return session.get('cart', {})

# Adding to cart
def add_to_cart(user_id, product_id, quantity):
    item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
    if item:
        item.quantity += quantity
    else:
        item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)
        db.session.add(item)
    db.session.commit()
