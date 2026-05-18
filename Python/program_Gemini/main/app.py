#app.py
from flask import Flask, render_template, request
import search
import add

# 템플릿 폴더 경로를 상위 폴더의 templates로 지정합니다.
app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_route():
    name = request.args.get('name')
    if name:
        results = search.search_student_by_name(name)
        return render_template('index.html', search_results=results, search_name=name)
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_route():
    student_id = request.form.get('id')
    name = request.form.get('name')
    mid = request.form.get('mid')
    final = request.form.get('final')
    
    if student_id and name and mid and final:
        new_student = add.insert_student(student_id, name, mid, final)
        return render_template('index.html', added_student=new_student)
    return render_template('index.html')

if __name__ == '__main__':
    # 외부 접속이 가능하도록 0.0.0.0으로 설정할 수 있으나 기본값으로 실행합니다.
    app.run(debug=True)