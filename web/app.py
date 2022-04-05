from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        'author':'Jav',
        'title': 'BlogPost',
        'content': 'Lorem ipsum',
        'date_posted': 'April 04, 2022'
    },

    {
        'author':'Jose',
        'title': 'Another BlogPost',
        'content': 'Lorem ipsum 22222',
        'date_posted': 'April 05, 2022'
    }


]



@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')





if __name__ == '__main__':
    app.run(debug=True)