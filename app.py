import os

import psycopg2
from uuid import uuid4
from openpyxl import Workbook
from flask import Flask, request, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

from os import path, getcwd

from misc import *

app = Flask(__name__)

db = ''
UPLOAD_FOLDER = path.join(getcwd(), 'menu')
ALLOWED_EXTENSIONS = {'xls', 'xlsx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@postgres:5432'
app.config['SECRET_KEY'] = 'amogus'

wb = Workbook()
wb = wb.active

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def test():
    return 'Hello World!'


@app.route('/add_menu', methods=['GET', 'POST'])
def add_menu():
    print(request.method)
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Не могу прочитать файл')
            return jsonify({'status': 'Can`t read file!'})
        file = request.files['file']
        if file.filename == '':
            flash('Нет выбранного файла')
            return jsonify({'status': 'No selected file!'})
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_origin = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_origin)
            add_food(file_origin)
        return jsonify({'status': 'success'})
    else:
        print(request.method)
        return jsonify({'gg': 'bruh'})


def main():
    app.run(port=5000, debug=True)


if __name__ == '__main__':
    main()
