from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/deals')
def deals():
    products = [
        {
            "name": "Alin Abstract Carpet",
            "image": "Alin Abstract Carpet",
            "old_price": "11,929.00",
            "name": "8,049.00",
            "sold_out": True,
            "url": "#"
        },
        {
              "name": "Alin Beige Dream Carpet",
            "image": "",
            "old_price": "11,929.00",
            "name": "8,049.00",
            "sold_out": True,
            "url": "#"
        }
        
        
        
        
        
        
    ]
    
    colors = ["A.Bej/A.Bej", "A.Gri/A.Gri", "A.Gri/A.Mavi", "A.Gri/Beyaz"]
    
    return render_template("dr_deals.html", products=products, colors=colors)