from flask import Flask, render_template, request
from time import strftime

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', The_title='Hello World!', the_main='My favourite game')

def log(name, phrase, time):
    with open('C:\\Users\\vladi\python_prj\mywebapp\\jurnal.log', 'a') as took:
        print(name,'wrote:', phrase, 'at', time, file=took)

@app.route('/res', methods=['POST'])
def res():
    log(request.form['name'], request.form['phrase'], strftime("%I:%M %p"))
    return render_template('res.html', the_name=request.form['name'], the_res=request.form['phrase'])


app.run(debug=True)