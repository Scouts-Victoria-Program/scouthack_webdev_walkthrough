#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)
fieldnames = ["author", "idea"]
database = "programs.csv"


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


@app.get("/program")
def list_programs():
    programs = []
    try:
        with open(database) as csvfile:
            csvreader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in csvreader:
                programs.append(row)
    except FileNotFoundError:
        pass

    return render_template("program.html", programs=programs)


@app.get("/program/new")
def new_program():
    return render_template("new_program.html")


@app.post("/program/new")
def new_program_post():
    program = {"author": request.form["author"], "idea": request.form["idea"]}
    with open(database, "a") as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writerow(program)

    return redirect(url_for("list_programs"))


if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
