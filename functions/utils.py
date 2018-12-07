#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from functions.tests import *
from functions.myglobals import *

def start_random_tell(file_path):
	with open(file_path, 'r') as file:
		read_in_ascii_format(file)

def read_in_ascii_format(file):
	amount = get_value('amount')
	length = get_value('length')
	epsilon = get_value('epsilon')
	for i in range(amount):	
		j = 0
		while 1:
			bit = file.read(1)
			if bit == '0' or bit == '1':
				epsilon.append(int(bit))
				j += 1
			else:
				continue
			if  j == length:
				break
		test_suite()
		del epsilon[:]

def test_suite():
	length = get_value('length')
	frequency(length)

def clear_list_in_dict(d):
	for key in d:
		del d[key][:]