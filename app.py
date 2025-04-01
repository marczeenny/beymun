from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from flask_compress import Compress
import csv

app = Flask(__name__, static_folder='static')
Compress(app)

@app.route('/')
def home():
    keys = ['id', 'q', 'a']
    data_list = []
    with open('data/faq.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data_list.append(dict(zip(keys, row)))
    return render_template('index.html', data_list=data_list)


@app.route('/about-us/')
def about_us():
    return render_template('about-us.html')


@app.route('/team/')
def team():
    keys = ['name', 'position', 'img']
    data_list = []
    with open('data/team.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data_list.append(dict(zip(keys, row)))
    return render_template('team.html', data_list=data_list)


@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')


@app.route('/beymun-2025/')
def beymun_2025():
    keys = ['name', 'size', 'level', 'desc', 'topic', 'logo', 'chair1', 'chair1pic', 'chair2', 'chair2pic', 'chair3', 'chair3pic']
    data_list = []
    with open('data/coms.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data_list.append(dict(zip(keys, row)))
    return render_template('beymun-2025.html', data_list=data_list)


@app.route('/register/')
def register():
    return render_template('register.html')


@app.route('/delegate-regist/')
def delegate_regist():
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSdw7V8QvQmZ-pVZW2zyuvWoMo4nEOqNKR-2_-iDH_0RnFdiYA/viewform?usp=dialog')


@app.route('/dais-regist/')
def dias_regist():
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLScSyGvmngW0M-B3l_GpQzizg5a2woA5t8pRWaP9OAg4pI37Qg/viewform?usp=header')


@app.route('/skl-regist/')
def skl_regist():
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSeQehJsIliEddOHRXlAaDBJ9CPgn_ha5zXxM_-N9vNcjbmXAg/viewform?usp=header')


@app.route('/int/')
def mymun():
    return redirect('https://mymun.com/conferences/beymun-2025')


@app.route('/awards/')
def awards():
    return send_from_directory('static', 'Recognition-guidelines.pdf/')


if __name__ == '__main__':
    app.run(debug=True)
