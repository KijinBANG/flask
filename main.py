from flask import Flask, request, render_template

app = Flask(__name__)  # flask 애플리케이션을 생성하는 코드


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/first/<int:num>')
def first(num):
    result = str(20 + num)
    return '20 + param = ' + result


@app.route('/second/<num>')
def second(num):
    result = "20" + num
    return '"20" + param = ' + result


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/calendar')
def calendar():
    return render_template('calendar.html')


@app.route('/param/', methods=['GET', 'POST'])
def param():
    print('This is for debugging.', request.method)
    if request.method == "POST":
        return 'post 요청'
    else:
        return 'get 요청'


def index():
    return 'index'


app.add_url_rule('/index', 'endpoint이름', index)


app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
