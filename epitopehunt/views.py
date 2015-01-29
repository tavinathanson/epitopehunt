from flask import Flask, render_template

from epitopehunt import app


@app.route('/')
def index():
    return render_template('index.html')
