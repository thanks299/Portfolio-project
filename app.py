from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')

@app.route('/contact', strict_slashes=False)
def contact():
    return render_template('contact.html')

@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')

@app.route('/skills', strict_slashes=False)
def skills():
    return render_template('skills.html')

if __name__ == '__main__':
    app.run(debug=True)
