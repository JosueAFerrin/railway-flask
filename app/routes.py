from flask import jsonify, render_template, Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    my_set = {"Hello World, my name is Josue"}
    return render_template('index.html', message=list(my_set))

@bp.route('/api')
def api():
    my_set = {"Hello World, my name is Josue"}
    return jsonify(list(my_set))
