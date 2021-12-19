from flask import Blueprint, request, make_response, jsonify, render_template
from sqlalchemy import text
from application import db
index_page = Blueprint('index_page', __name__)


@index_page.route('/')
def index_page_index():
    return 'index page'


@index_page.route('/me')
def hello():
    return 'hello, i love cxd'


@index_page.route('/get')
def get():
    req = request.values
    var_a = req['a'] if 'a' in req else 'i like susu'
    return 'request:%s,params:%s,var_a:%s' % (request.method, request.args, var_a)


@index_page.route('/post', methods=['POST'])
def post():
    # var_a = request.form['a'] if 'a' in request.form else ''
    req = request.values
    var_a = req['a'] if 'a' in req else 'i like susu'
    return 'request %s, params:%s, var_a:%s' % (request.method, request.form, var_a)


@index_page.route('/upload', methods=['POST'])
def up_load():
    f = request.files
    return 'request %s, params:%s, file:%s' % (request.method, request.files, f)


@index_page.route('/text')
def text_a():
    response = make_response('hello world', 200)
    return response


@index_page.route('/json')
def json():
    import json
    data = {'a': 'b'}
    # response = make_response(json.dumps(data))
    response = make_response(jsonify(data))
    # response.headers['Content-Type'] = 'application/json'
    return response


@index_page.route('/template')
def template():
    name = 'susu'
    con = {'name': name, 'user': {'nickname': "ilikesusu", 'QQ': '869752095', 'email': 'xxxxxx@163.com'},
           'numlist': {1, 2, 3, 4, 5}}


    # 数据库查询

    sql = text("select * from user")
    result = db.engine.execute(sql)
    con['result'] = result
    return render_template('index.html', **con)


@index_page.route('/extend_template')
def extend_template():
    return render_template('extend_template.html')


@index_page.route('/extend_template_other')
def extend_template_other():
    return render_template('extend_template_other.html')
