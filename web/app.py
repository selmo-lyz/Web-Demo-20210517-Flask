from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/research")
def research():
    return render_template('research.html')

@app.route("/people")
def people():
    return render_template('people.html')

@app.route("/alumni")
def alumni():
    return render_template('alumni.html')

@app.route("/publication")
def publication():
    return render_template('publication.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')