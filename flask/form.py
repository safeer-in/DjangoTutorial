#!/usr/bin/env python

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])

def index():
	if request.method == "POST":
		un = request.form['username']
		pw = request.form['password']
		print un,pw
		return "ok"
	else:
		return render_template("form.html")

if __name__ == "__main__":
	app.run()