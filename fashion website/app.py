from flask import Flask, render_template

app = Flask(__name__)

# Sample data - in a real application, this would come from a database
products = [
    {"id": 1, "name": "Summer Dress", "description": "Light and breezy summer dress", "price": 59.99},
    {"id": 2, "name": "Denim Jacket", "description": "Classic denim jacket", "price": 79.99},
    {"id": 3, "name": "Silk Scarf", "description": "Elegant silk scarf", "price": 29.99},
]
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/products')
def product_list():
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)