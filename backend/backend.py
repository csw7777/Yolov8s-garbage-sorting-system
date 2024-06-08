from flask import Flask, request, jsonify
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template
import sqlite3
import datetime
import base64
import ast

def create_database():

    conn = sqlite3.connect('C:/Users/14794/yolov8/code_yolov8/output/XTS.db')

    c = conn.cursor()

    # 创建用户表

    c.execute('''CREATE TABLE IF NOT EXISTS user (

        id INTEGER PRIMARY KEY AUTOINCREMENT, 

        username TEXT, 

        password TEXT)''')

    # 创建结果表

    c.execute('''CREATE TABLE IF NOT EXISTS results (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        image_name TEXT,

        input_time TEXT,

        results TEXT,

        num_objects INTEGER,

        process_time TEXT,

        result_image_path TEXT)''')

    # 创建图片表，包含图片数据

    c.execute('''CREATE TABLE IF NOT EXISTS images (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        image_data BLOB,

        recognition_time TEXT)''')

    conn.commit()

    conn.close()
    
create_database()

def get_user_results(username):

    conn = sqlite3.connect('C:/Users/14794/yolov8/code_yolov8/output/XTS.db')

    c = conn.cursor()

    c.execute("SELECT results,input_time FROM results WHERE username=?", (username,))    

    rsl = c.fetchall()
    
    results = [([i[0] for i in ast.literal_eval(i[0])],[i[1]*100 for i in ast.literal_eval(i[0])],i[1]) for i in rsl]
    
    c.execute("SELECT image_data,recognition_time FROM images WHERE username=?", (username,))    
    
    imgs = c.fetchall()
    
    imgs = [(base64.b64encode(img[0]).decode('utf-8'), img[1]) for img in imgs]

    conn.close()
    
    rsldic={'img':imgs,'rsl':results}

    return rsldic


def add_test_data():

    conn = sqlite3.connect('C:/Users/14794/yolov8/code_yolov8/output/XTS.db')

    c = conn.cursor()

    # 检查是否已存在相同的用户名，避免重复添加

    c.execute("SELECT * FROM user WHERE username='csw'")

    if not c.fetchone():

        c.execute("INSERT INTO user (username, password) VALUES (?, ?)", ('csw', '123'))

        conn.commit()

    conn.close()



add_test_data()  # 调用此函数以添加测试数据

app = Flask(__name__)


@app.route('/login', methods=['POST'])

def login():

    username = request.json['username']

    password = request.json['password']

    conn = sqlite3.connect('C:/Users/14794/yolov8/code_yolov8/output/XTS.db')

    c = conn.cursor()

    c.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))

    account = c.fetchone()

    conn.close()

    if account:

        return jsonify(success=True), 200

    else:

        return jsonify(success=False), 401

@app.route('/')

def index():

    conn = sqlite3.connect('C:/Users/14794/yolov8/code_yolov8/output/XTS.db')

    c = conn.cursor()

    c.execute("SELECT * FROM user")

    users = c.fetchall()

    conn.close()

    return render_template('user_db.html', users=users)


@app.route('/personal-center')

def personal_center():

    # 从 query string 获取用户名
    
    username = request.args.get('username', 'Guest')
    
    user_results = get_user_results(username)

    return render_template('personal_center.html', username=username, user_results=user_results,zip=zip)


@app.route('/quiz')

def quiz():

    # 从 query string 获取用户名
    
    username = request.args.get('username', 'Guest')

    return render_template('quiz.html', username=username)


@app.route('/feedback')

def feedback():

    # 从 query string 获取用户名
    
    username = request.args.get('username', 'Guest')

    return render_template('feedback.html', username=username)


@app.route('/nearby')

def nearby():

    # 从 query string 获取用户名
    
    username = request.args.get('username', 'Guest')

    return render_template('nearby.html', username=username)



@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])

def users():

    conn = sqlite3.connect('C:/Users/14794/yolov8/code_yolov8/output/XTS.db')

    c = conn.cursor()


    if request.method == 'GET':

        c.execute("SELECT * FROM user")

        users = c.fetchall()

        return jsonify(users)


    if request.method == 'POST':

        data = request.get_json()

        username = data.get('username')

        password = data.get('password')

        # 检查用户名和密码是否为空

        if not username or not password:

            conn.close()

            return jsonify({'success': False, 'message': '用户名或密码不能为空'}), 400

        # 检查用户名是否已存在

        c.execute("SELECT * FROM user WHERE username=?", (username,))

        if c.fetchone():

            conn.close()

            return jsonify({'success': False, 'message': '用户名已存在'}), 409
        
        # 插入新用户

        c.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))

        conn.commit()

        conn.close()

        return jsonify({'success': True}), 201


    if request.method == 'PUT':

        id = request.json['id']

        username = request.json['username']

        password = request.json['password']

        c.execute("UPDATE user SET username=?, password=? WHERE id=?", (username, password, id))

        conn.commit()

        return jsonify(success=True), 200


    if request.method == 'DELETE':

        username = request.args.get('username')

        c.execute("DELETE FROM user WHERE username=?", (username,))

        affected_rows = c.rowcount

        conn.commit()

        if affected_rows == 0:

            return jsonify({'success': False, 'message': '没有找到用户'}), 404

        return jsonify(success=True), 200



    conn.close()


@app.route('/search_user')

def search_user():

    username = request.args.get('username')

    conn = sqlite3.connect('C:/Users/14794/yolov8/code_yolov8/output/XTS.db')

    c = conn.cursor()

    c.execute("SELECT * FROM user WHERE username=?", (username,))

    user = c.fetchone()

    conn.close()

    if user:

        return jsonify({'success': True, 'user': {'username': user[1], 'password': user[2]}})

    else:

        return jsonify({'success': False})


if __name__ == '__main__':

    app.run(debug=True)