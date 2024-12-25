from flask import Flask, render_template, request, redirect, url_for
from models import Task, init_db, get_all_tasks, add_task, update_task_status, delete_task

app = Flask( __name__ )

# Initialize the database
init_db()

@app.route('/')
def index():
    tasks = get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_new_task():
    task_name = request.form['task_name']
    if task_name:
        add_task(Task(task_name))
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    update_task_status(task_id, 'complete')
    return redirect(url_for('index'))

@app.route('/incomplete/<int:task_id>')
def incomplete_task(task_id):
    update_task_status(task_id, 'incomplete')
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task_entry(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
