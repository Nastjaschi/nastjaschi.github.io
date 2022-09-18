from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():

    return render_template('main_unauthorized.html')


@app.route("/loggedin/")
def logged_main():

    return render_template('main_logged.html')


@app.route("/admin/")
def logged_admin():

    return render_template('main_admin.html')


@app.route("/review_form/")
def review_form():

    return render_template('leave_review.html')
    
@app.route("/new_course/")
def new_course():

    return render_template('new_course.html')


@app.route("/admin_new_courses/")
def admin_new_courses():

    return render_template('admin_new_courses.html')
