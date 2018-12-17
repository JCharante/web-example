from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

hits = 0
todos = []


@app.route('/')
def index():
    global hits, todos
    hits = hits + 1
    return render_template("index.html", hits=hits, todos=todos)


@app.route('/add', methods=['POST'])
def add():
    global todos
    todos.append(request.form['todo'])
    return redirect(url_for('index'))


app.run(host='0.0.0.0', port=8080, debug=True)
