from flask import Flask, url_for, redirect, render_template
import os
app = Flask(__name__)

@app.route('/')
def index():
    title = "Home"
    name = "Home"
    return render_template('index.html', title=title, name=name)

@app.route("/doctor.html")
def doctor():
    return render_template('doctor.html')

if __name__ == "__main__":
    host = os.popen('hostname -I').read()
    app.run(host='0.0.0.0', port=80, debug=False)