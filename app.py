from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): return render_template('index.html')

@app.route('/sales')
def sales(): return render_template('sales.html')

@app.route('/price')
def price(): return render_template('price.html')

@app.route('/witness')
def witness(): return render_template('witness.html')

@app.route('/partners')
def partners(): return render_template('partners.html')

@app.route('/contact')
def contact(): return render_template('contact.html')

@app.route('/login')
def login(): return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
