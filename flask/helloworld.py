#!/usr/bin/env python

from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
@app.route("/index")

def index():
	#return "<center><h1>Hello World!</h1></center>"
	return render_template("hello.html",name="Bingo")

if __name__ == "__main__":
	app.run()