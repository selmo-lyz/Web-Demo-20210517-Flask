from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/research.html")
def research():
    return render_template('research.html')

@app.route("/people.html")
def people():
    return render_template('people.html')

@app.route("/alumni.html")
def alumni():
    return render_template('alumni.html')

@app.route("/publication.html")
def publication():
    return render_template('publication.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')