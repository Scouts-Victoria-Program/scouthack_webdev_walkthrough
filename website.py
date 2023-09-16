#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("patrol.html")


@app.get("/my-page")
def my_page():
    return render_template("my-page.html")


@app.get("/hello/")
@app.get("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
