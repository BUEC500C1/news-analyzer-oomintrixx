from flask import render_template, request, flash, redirect, url_for
from . import main
from ..models import File
from .. import db
from ..file.file_upload_helper import _generateText, convert_binary


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<username>')
def user(username):

    return render_template('user.html', user=user)

@main.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['inputFile']
        file.save(file.filename)
        text = convert_binary(file.filename)
        newFile = File(name=file.filename, data=file.read(), text=text)
        db.session.add(newFile)
        db.session.commit()
        flash('file uploaded sucessfully!')
        return redirect(url_for('main.index'))
    else:
        return render_template('file/file_upload.html')
'''
@main.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
'''
