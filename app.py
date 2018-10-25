from flask import Flask
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def home():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
