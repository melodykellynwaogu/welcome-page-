from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'items.json'

def load_items():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_items(items):
    with open(DATA_FILE, 'w') as f:
        json.dump(items, f)

@app.route('/')
def index():
    items = load_items()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item = request.form.get('item')
        if item:
            items = load_items()
            items.append(item)
            save_items(items)
        return redirect(url_for('index'))
    return render_template('add_item.html')

if __name__ == '__main__':
    app.run(debug=True)