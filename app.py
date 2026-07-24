from flask import Flask, render_template, Response

app = Flask(__name__)

# --- 這是你負責的「Python 寫 CSS」部分 ---
CSS_CONTENT = """
:root { --yellow: #FFD700; --green: #2e7d32; }
body { font-family: Arial, sans-serif; margin: 0; background: #f4f4f9; }
nav { background: var(--yellow); padding: 15px; display: flex; justify-content: center; gap: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
nav a { text-decoration: none; color: #333; font-weight: bold; }
.content { max-width: 1000px; margin: 30px auto; padding: 20px; min-height: 70vh; background: white; border-radius: 10px; }
.card { border: 1px solid #ddd; padding: 20px; border-radius: 10px; text-align: center; width: 250px; margin: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
.btn { background: var(--green); color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block; margin-top: 10px; }
footer { background: #333; color: white; text-align: center; padding: 20px; margin-top: 40px; font-size: 12px; }
"""

@app.route('/style.css')
def style():
    return Response(CSS_CONTENT, mimetype='text/css')
# ---------------------------------------

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
