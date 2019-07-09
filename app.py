from flask import Flask, render_template

app = Flask(__name__)

# If you look in folder view of this project there are two folders as static and template
# static folder -> Only css, scripts and files which are never gonna change
# templates -> HTML files which serves as structure of the website
@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", username=username)


@app.route('/')
def index():
    return "Hello World"

# Mapping Multiple URLs
@app.route('/signup')
@app.route('/<user_page>')
def user(user_page=None):
    return render_template("user.html", user_page=user_page)

# Passing objects in Templates
@app.route('/check_list')
def check_list():
    l = ["food", "drink", "breath"]
    return render_template("check_list.html", l=l)


if __name__ == '__main__':
    app.run()


