from flask import Flask
from flask import request, redirect, url_for, render_template
import os

from database import get_items, add_task, delete_task, update_completed_task, get_db_connection

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE=os.path.join(basedir,'test_items.db')

app = Flask(__name__)

app.config.from_mapping(
    DATABASE=DATABASE)

@app.route('/')
def index():
    test_items = get_items('test_items.db')
    return render_template('index.html', items=test_items)

@app.route('/sort', methods = ['GET'])
def sort():
    sort_by = request.args.get('sort_by', default='')
    return redirect(url_for('index', sort_by=sort_by))

@app.route('/add_item/', methods= ['POST'])
def add_item():
    new_item = request.form['new_item']
    add_task(DATABASE, new_item)
    return redirect(url_for(('index')))

@app.route('/update_item/', methods = ['POST'])
def update_item():
    item_id = request.form.get('item_id')
    done = request.form.get('done')
    done_int = 1 if done == 'on' else 0
    update_completed_task(DATABASE, item_id, done_int)
    return redirect(url_for('index'))

@app.route('/delete/', methods=['POST'])
def delete():
    item_id = request.form.get('item_id')
    delete_task(DATABASE, item_id)
    return redirect(url_for(('index')))

@app.teardown_appcontext
def close_db_connection(exception):
    conn = getattr(app, '_database', None)
    if conn is not None:
        conn.close()

def init_db():
    conn = get_db_connection(DATABASE)
    with app.open_resource('schema.sql', mode='r') as f:
        conn.executescript(f.read())
    conn.close()

# run the app
if __name__ == '__main__':
    #init_db()
    app.run(port=8000, debug=True)
