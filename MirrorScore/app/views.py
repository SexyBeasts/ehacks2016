import os
#from flask import Flask
from flask import render_template, request, redirect, url_for, send_from_directory, json
from hertzReader import freqCount
from app import app

app.config['UPLOAD_FOLDER'] = 'app\wavComps'
app.config['ALLOWED_EXTENSIONS'] = set(['wav'])

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
	
@app.route('/audioLoad', methods = ['POST', 'GET'])
def audioLoad():
	print("finding nemo...")
	file = request.files['WORKDAMMIT']
	print("saving file...")
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
	print("uploading file...")
	noteArray = freqCount(app.config['UPLOAD_FOLDER'] + "/" + file.filename)
	noteArray = json.dumps(noteArray)
	print(noteArray)
	return render_template('/notes.html')