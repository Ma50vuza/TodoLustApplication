from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask (__name__)

API_URL = "https://todo-backend-liyx.onrender.com/api/todo_entries"

@app.route('/')
def index():

        response = requests.get(API_URL)
        todos = response.json()
        #todos = []
        return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    if name:
        requests.post(API_URL, json={"name": name})
    return redirect('/')

@app.route('/update/<item_id>', methods=['POST'])
def update(item_id):
    name = request.form.get('name')
    if name:
        requests.put(f"{API_URL}/{item_id}", json={"name": name})
    return redirect('/')

@app.route('/delete/<item_id>', methods=['POST'])
def delete(item_id):
    requests.delete(f"{API_URL}/{item_id}")
    return redirect('/')

if __name__== '__main__':
    app.run(debug=True)


