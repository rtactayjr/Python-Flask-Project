  from flask import Flask, render_template, url_for
from datetime import date
import requests

posts = requests.get("https://api.npoint.io/2469a22cab4589fbed43").json()

app = Flask(__name__)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', year=year, all_posts=posts)

@app.route('/about')
def about():
	return render_template('about.html', year=year)

@app.route('/contact')
def contact():
	return render_template('contact.html', year=year)

@app.route('/post')
def post():
	return render_template('post.html', year=year)


if __name__ == '__main__':
	year = str(date.today().year)
	app.run(debug=True)
