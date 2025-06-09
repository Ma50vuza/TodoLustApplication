from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask (__name__)

@app.route('/', methods=["GET"])
def index():
    print(url_for('add_task'))
    response = requests.get("https://todo-backend-liyx.onrender.com/api/todo_entries")
    data = response.json()
    return render_template('index.html', todos=data)

@app.route('/<id>')
def delete_by_id(id):
    response = requests.delete(f"https://todo-backend-liyx.onrender.com/api/todo_entries/{id}")
    
    return redirect(url_for('index'))

@app.route('/add', methods=["POST"])
def add_task():
        name = request.form.get("name")
        response = requests.post("https://todo-backend-liyx.onrender.com/api/todo_entries", json={'name': name})
        print(response.status_code)
        return redirect(url_for('index'))

@app.route('/edit/<id>', methods=["POST", "GET"])
def update_task(id):
    response = requests.get("https://todo-backend-liyx.onrender.com/api/todo_entries")
    todos = response.json()
    todo = ""
    for todo_ in todos:
         if todo_['id']==  id:
              todo = todo_['name']
    if request.method == "POST":
         
        name = request.form.get("name")
        if name:
            response = requests.put(f"https://todo-backend-liyx.onrender.com/api/todo_entries/{id}", json={"name": name})
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
    return render_template("edit.html", todo=todo)



if __name__== '__main__':
    app.run(debug=True)


