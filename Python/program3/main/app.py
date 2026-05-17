from flask import Flask, render_template, request
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    from search import search_student
    name = request.args.get('name', '')
    results = search_student(name)
    return render_template('index.html', results=results, search_name=name)

@app.route('/add', methods=['POST'])
def add():
    from add import add_student
    student_id = request.form.get('id')
    name = request.form.get('name')
    mid = float(request.form.get('mid'))
    final = float(request.form.get('final'))
    message = add_student(student_id, name, mid, final)
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)