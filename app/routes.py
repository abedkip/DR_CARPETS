from app import app
from flask import render_template


@app.route('/')
def Home():
    return render_template('homepage.html')


# COLORS DROPDOWN
# black
@app.route('/colors/<color_name>')
def show_color(color_name):
    # Basic validation and fallback
    valid_colors = ['black', 'blue', 'brown', 'red', 'grey']
    if color_name.lower() not in valid_colors:
        return f"Color '{color_name}' not found", 404

    return render_template('black.html', color=color_name.lower())

# blue
@app.route('/colors/<blue>')
def blue_color(color_name):
    # Basic validation and fallback
    valid_colors = ['black', 'blue', 'brown', 'red', 'grey']
    if color_name.lower() not in valid_colors:
        return f"Color '{color_name}' not found", 404

    return render_template('blue.html', color=color_name.lower())
@app.route('/colors/<blue>')
def blue_color(color_name):
    # Basic validation and fallback
    valid_colors = ['black', 'blue', 'brown', 'red', 'grey']
    if color_name.lower() not in valid_colors:
        return f"Color '{color_name}' not found", 404

    return render_template('grey.html', color=color_name.lower())


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