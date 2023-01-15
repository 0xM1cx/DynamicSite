from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> Hello</h1>"

