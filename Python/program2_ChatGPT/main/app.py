from flask import Flask, render_template, request
from search import search_student
from add import add_student

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name')

    students = []

    if name:
        students = search_student(name)

    return render_template(
        'index.html',
        students=students,
        message='검색 완료'
    )


@app.route('/add', methods=['POST'])
def add():
    student_id = request.form.get('id')
    name = request.form.get('name')
    mid = request.form.get('mid')
    final = request.form.get('final')

    add_student(student_id, name, mid, final)

    students = search_student(name)

    return render_template(
        'index.html',
        students=students,
        message='학생 추가 완료'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)