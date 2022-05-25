from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
def my_index():
    return render_template('index.html', token="hlo-flask-react")

@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)

    # from flask import Flask


# app = Flask(__name__)


# @app.route('/')
# def home():
#     return 'Home Page Route'


# @app.route('/about')
# def about():
#     return 'About Page Route'


# @app.route('/portfolio')
# def portfolio():
#     return 'Portfolio Page Route'


# @app.route('/contact')
# def contact():
#     return 'Contact Page Route'


# @app.route('/api')
# def api():
#     with open('data.json', mode='r') as my_file:
#         text = my_file.read()
#         return text