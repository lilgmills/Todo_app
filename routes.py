from flask import Flask
from flask import request, redirect, url_for, render_template
import os

from database import get_items, get_current_list_name, update_list_name, add_task, delete_task, update_completed_task, create_schema, get_db_connection
from database import current_todo_id

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE=os.path.join(basedir,'test_items.db')

app = Flask(__name__)

app.config.from_mapping(
    DATABASE=DATABASE)

@app.route('/')
def index():
    test_items = get_items(DATABASE, current_todo_id)
    todo_list_name = get_current_list_name(DATABASE, current_todo_id)
    return render_template('index.html', items=test_items, todo_list_name=todo_list_name)

@app.route('/sort', methods = ['GET'])
def sort():
    sort_by = request.args.get('sort_by', default='')
    return redirect(url_for('index', sort_by=sort_by))

@app.route('/add_item/', methods= ['POST'])
def add_item():
    new_item = request.form['new_item']
    add_task(DATABASE, new_item, current_todo_id)
    return redirect(url_for(('index')))

@app.route('/update_todo_list_name', methods=['POST'])
def update_todo_list_name():
    new_name = request.json['new_name']
    todo_list_id = current_todo_id
    update_list_name(DATABASE, todo_list_id, new_name)
    return redirect(url_for(('index')))


@app.route('/update_item/', methods = ['POST'])
def update_item():
    item_id = request.form.get('item_id')
    done = request.form.get('done')
    done_int = 1 if done == 'on' else 0
    update_completed_task(DATABASE, item_id, done_int)
    return redirect(url_for('index'))

@app.route('/new_edit/', methods=['GET', 'POST'])
def new_edit():
    if request.method == 'POST':
        item_id = request.form['item_id']
        desc = request.form['desc']
        return render_template('edit_item.html', item_id=item_id, desc=desc)
    else:
        return redirect(url_for('index'))

@app.route('/post_edit/', methods = ['GET','POST'])
def post_edit():
    item_id = request.form['item_id']
    new_text = request.form['new_text']
    edit_task(DATABASE, item_id, new_text)
    return redirect(url_for(('index')))
    

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
    
    create_schema(DATABASE)
    app.run(port=8000, debug=True)
