from flask import Flask, url_for, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    title = "Home"
    name = "Home"
    return render_template('index.html', title=title, name=name)

@app.route('/doctor')
def doctor():
    title = "Doctor"
    name = "Doctor"
    return redirect(url_for('doctor.html'), title=title, name=name)

if __name__ == "__main__":
    app.run()