from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session

@app.route('/')
def index():
    items = session.get('items', [])
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item = request.form.get('item')
        if item:
            items = session.get('items', [])
            items.append(item)
            session['items'] = items
        return redirect(url_for('index'))
    return render_template('add_item.html')

@app.route('/delete/<int:index>', methods=['POST'])
def delete_item(index):
    items = session.get('items', [])
    if 0 <= index < len(items):
        items.pop(index)
        session['items'] = items
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()