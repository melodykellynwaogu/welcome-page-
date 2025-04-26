from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store items
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item = request.form.get('item')
        if item:
            items.append(item)
        return redirect(url_for('index'))
    return render_template('add_item.html')

if __name__ == '__main__':
    app.run()  # Removed debug=True for production deployment