# app.py

from flask import Flask, render_template

app = Flask(__name__)

# Route for the Home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the Dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route for the Story page
@app.route('/story')
def story():
    return render_template('story.html')

if __name__ == '__main__':
    # Run the Flask app in debug mode (useful for development)
    app.run(debug=True)