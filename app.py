from flask import Flask, render_template, request
from get_json import get_json
from parse_json import parse_json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teach')
def teach():
    return render_template('teach.html')

@app.route('/speech')
def speech():
    return render_template('speech.html')

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        user_input = request.form['subject']
        questions = get_json(user_input)
        return questions
    return render_template('write.html')

if __name__ == '__main__':
    app.run()
