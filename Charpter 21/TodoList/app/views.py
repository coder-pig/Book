from app import app, db
from flask import render_template, request
from app.models import ToDo, ToDoForm
import datetime


@app.route('/')
def index():
    form = ToDoForm(request.form)
    todos = ToDo.query.order_by(ToDo.time.desc())
    return render_template("index.html", todos=todos, form=form)


@app.route('/add', methods=['POST'])
def add_todo():
    form = ToDoForm(request.form)
    if form.validate_on_submit():
        content = form.todo.data
        todo = ToDo()
        todo.content = content
        todo.time = datetime.datetime.now()
        db.session.add(todo)
        db.session.commit()
    todos = ToDo.query.order_by(ToDo.time.desc())
    return render_template("index.html", todos=todos, form=form)


@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    form = ToDoForm()
    todo = ToDo.query.filter(ToDo._id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    todos = ToDo.query.order_by(ToDo.time.desc())
    return render_template("index.html", todos=todos, form=form)


@app.route('/done/<int:todo_id>')
def done_todo(todo_id):
    form = ToDoForm()
    todo = ToDo.query.filter(ToDo._id == todo_id).first()
    todo.status = 1
    db.session.commit()
    todos = ToDo.query.order_by(ToDo.time.desc())
    return render_template("index.html", todos=todos, form=form)


@app.route('/nodone/<int:todo_id>')
def nodone_todo(todo_id):
    form = ToDoForm()
    todo = ToDo.query.filter(ToDo._id == todo_id).first()
    todo.status = 0
    db.session.commit()
    todos = ToDo.query.order_by(ToDo.time.desc())
    return render_template("index.html", todos=todos, form=form)
