#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import (Flask, render_template, abort, request,
                   jsonify, send_from_directory)
from models.engine.DBStorage import DBStorage
from flask_cors import CORS


app = Flask(__name__)

CORS(app)
app.template_folder = 'web_static/'


@app.route('/users/', methods=['GET'], strict_slashes=False)
def get_bmi():
    """ Login """
    global secret, date_of_birth
    db_storage = DBStorage()
    username = request.args.get('username')
    data_user = db_storage.user(username)
    for data in data_user:
        date_of_birth = data.date_of_birth
    if not username:
        abort(401, "enter username")
    password = request.args.get('password')
    if not password:
        abort(401, "enter password")
    try:
        data = db_storage.get_bmi_user(username)
    except Exception:
        abort(401, "User doesn't Exit")
    dictionary = {}
    i = 0
    for user, bmi_record in data:
        i = i + 1
        dictionary[i] = bmi_record.bmi
        secret = user.password
    if secret != password:
        abort(401, "Wrong password")
    return render_template('1-users.html', username=username,
                           date_of_birth=date_of_birth, bmi_record=dictionary)


@app.route('/user/info', methods=['GET'], strict_slashes=False)
def get_user():
    """ Getting user information """
    db_storage = DBStorage()
    username = request.args.get('username')
    user_data = db_storage.user(username)
    dictionary = {}
    for data in user_data:
        dictionary["first_name"] = data.first_name
        dictionary["last_name"] = data.last_name
    return jsonify(dictionary)


@app.route('/', strict_slashes=False)
def login():
    """ Login page"""
    return render_template('login.html')


@app.route('/styles/style.css')
def serve_login_css():
    """ Route to serve css file """
    filename = 'style.css'
    return send_from_directory('web_static/styles/', filename)


@app.route('/scripts/login.js')
def serve_login_js():
    """ Route to serve script file """
    filename = 'login.js'
    return send_from_directory('web_static/scripts/', filename)


@app.route('/users/images/logout.png')
def serve_logout():
    """ Route to serve png file """
    filename = 'logout.png'
    return send_from_directory('web_static/images/', filename)


@app.route('/users/add/', methods=['POST'])
def add_user():
    """Adding user"""
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        last_name = request.form.get('last_name')
        first_name = request.form.get('first_name')
        sex = request.form.get('sex')
        date_of_birth = request.form.get('date_of_birth')
        db_storage = DBStorage()
        db_storage.add_user(username, first_name, last_name, sex, email,
                            password, date_of_birth)
        db_storage.add_bmi(username, 1, 0)
        return jsonify({'success': True, 'message': 'User added successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/users/<username>', methods=['DELETE'])
def del_user(username):
    """ Deleting User"""
    try:
        db_storage = DBStorage()
        username = request.form.get('username')
        db_storage.delete_user(username)
        return jsonify({'success': True,
                        'message': 'User Deleted successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/users/styles/style-user.css')
def serve_css():
    """ Route to serve css file """
    filename = 'style-user.css'
    return send_from_directory('web_static/styles/', filename)


@app.route('/users/data/chart-2015.pdf')
def serve_pdf_boys():
    """ Route to serve pdf1 file """
    filename = 'chart-2015.pdf'
    return send_from_directory('web_static/data/', filename)


@app.route('/users/data/chart-2016.pdf')
def serve_pdf_girls():
    """ Route to serve pdf2 file """
    filename = 'chart-2016.pdf'
    return send_from_directory('web_static/data/', filename)


@app.route('/users/images/Bmi.jpg')
def serve_jpg():
    """ Route to serve jpg file """
    filename = 'Bmi.jpg'
    return send_from_directory('web_static/images/', filename)


@app.route('/users/scripts/user.js')
def serve_script():
    """ Route to serve script file """
    filename = 'user.js'
    return send_from_directory('web_static/scripts/', filename)


@app.route('/users/images/icon.png')
def serve_png():
    """ Route to serve png file """
    filename = 'icon.png'
    return send_from_directory('web_static/images/', filename)


@app.route('/images/icon.png')
def serve_login_png():
    """ Route to serve png file """
    filename = 'icon.png'
    return send_from_directory('web_static/images/', filename)


@app.route('/users/bmi/', methods=['POST'])
def add_bmi():
    """ Adding height and weight for a user"""
    try:
        db_storage = DBStorage()
        username = request.args.get('username')
        height = request.args.get('height')
        weight = request.args.get('weight')
        db_storage.add_bmi(username, int(height), int(weight))
        db_storage.close()
        return jsonify({'success': True,
                        'message': 'User BMI added successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == "__main__":
    """ Main Function """
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
