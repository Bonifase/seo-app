from flask import render_template
from flask import Flask, render_template
from urllib.request import urlopen
from bs4 import BeautifulSoup
from seo import app


@app.route("/")
def home():
    return render_template('index.html')
