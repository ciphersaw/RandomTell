#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'Cipher Saw'

from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
from functions.tests import *
from functions.utils import *
from functions import myglobals
import os

myglobals._init()
p_value_dict = myglobals.get_value('p_value_dict')

UPLOAD_FOLDER = 'uploads'

file_path = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/test', methods = ['GET', 'POST'])
def randomness_test():
	global file_path
	if request.method == 'POST':
		if 'file' in request.files:
			file = request.files['file']
			filename = secure_filename(file.filename)
			file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(file_path)
			return redirect(url_for('randomness_test', filename = filename))
		elif 'start' in request.form:
			clear_list_in_dict(p_value_dict)
			if 'filename' in request.args:
				filename = secure_filename(request.args.get('filename'))
				file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			myglobals.set_value('amount', int(request.form['amount']))
			myglobals.set_value('length', int(request.form['length']))
			start_random_tell(file_path)
			return "Complete!"
	return render_template('test.html')

@app.route('/result')
def result_display():
	return render_template('result.html', p_value_dict = p_value_dict)

if __name__ == '__main__':
	app.run(debug = True)