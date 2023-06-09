from flask import Flask, render_template, request
from get_json import get_json
from parse_json import parse_json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/Signup')
def Signup():
    return render_template('Signup.html')


@app.route('/teach')
def teach():
    return render_template('teach.html')

@app.route('/speech')
def speech():
    return render_template('speech.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/choose')
def choose():
    return render_template('choose.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/speechToText2', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        user_input = request.form['message']
        questions = get_json(user_input)
        return questions
    return render_template('speechToText2.html')

if __name__ == '__main__':
    app.run(debug=True)
