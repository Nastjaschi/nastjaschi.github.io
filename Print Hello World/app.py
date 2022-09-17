from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")
def home():

 

    return render_template('main_unauthorized.html')

@app.route("/loggedin")
def logged_main():

    return render_template('main_logged.html')