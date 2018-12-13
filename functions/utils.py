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
	is_selected = get_value('is_selected')
	block_length_of_frequency_within_a_block = get_value('block_length_of_frequency_within_a_block')
	if is_selected['frequencyTest']:
		frequency(length)
	if is_selected['frequencyTestWithinABlock']:
		frequency_within_a_block(block_length_of_frequency_within_a_block, length)

def clear_list_in_dict(d):
	for key in d:
		del d[key][:]