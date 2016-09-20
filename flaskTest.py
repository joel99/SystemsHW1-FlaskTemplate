from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "This is my home page."

@app.route("/bold")
def bold():
    return "<b>A brave new world.</b>"

@app.route("/link")
def link():
    return '<a href = "/"> Link to home </a>'

if __name__ == "__main__":
    app.run()
