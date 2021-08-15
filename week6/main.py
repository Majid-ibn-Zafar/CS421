from flask import Flask
app = Flask (__name__)

@app.route('/')
def index():
    return '<h1> Hello World! </h1>'

@app.route('/contact-us')
def info():
    return '<h2> Contact US</h2>'

@app.route('/users/<username>')
def userprofile(username):
    return '<h3> This is a profile page for {}</h1>'.format(username)

if __name__ == "__main__":
    app.run(port=5000)