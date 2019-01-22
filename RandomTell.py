#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'Cipher Saw'

from flask import Flask, request, redirect, url_for, render_template, jsonify
from werkzeug import secure_filename
from functions.utils import *
import os

global_variables_initialization()
p_value_dict = get_value('p_value_dict')

UPLOAD_FOLDER = 'uploads'

file_path = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	return redirect(url_for('randomness_test'))

@app.route('/test', methods = ['GET', 'POST'])
def randomness_test():
	global file_path
	if request.method == 'POST':
		if 'file' in request.files:
			file = request.files['file']
			file_name = secure_filename(file.filename)
			file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
			file.save(file_path)
			return jsonify({'success': 0})
		elif 'start' in request.json:
			clear_list_in_dict(p_value_dict)
			set_value('amount', int(request.json['amount']))
			set_value('length', int(request.json['length']))
			set_value('block_length_of_frequency_within_a_block', int(request.json['blockLengthOfFTWAB']))
			set_value('is_selected', request.json['isSelected'])
			return jsonify(start_random_tell(file_path))
	return render_template('test.html')

@app.route('/result')
def result_display():
	return render_template('result.html', p_value_dict = p_value_dict)

if __name__ == '__main__':
	app.run(debug=True)