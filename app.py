from flask import Flask, render_template, redirect, url_for, request, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about-us')
def about_us():
    return render_template('about-us.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/beymun-2025')
def beymun_2025():
    return render_template('beymun-2025.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/delegate-regist')
def delegate_regist():
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSdw7V8QvQmZ-pVZW2zyuvWoMo4nEOqNKR-2_-iDH_0RnFdiYA/viewform?usp=dialog')


@app.route('/dais-regist')
def dias_regist():
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLScSyGvmngW0M-B3l_GpQzizg5a2woA5t8pRWaP9OAg4pI37Qg/viewform?usp=header')


if __name__ == '__main__':
    app.run(debug=True)
