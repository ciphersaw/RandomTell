#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from functions.tests import *

def start_random_tell(file_path):
	with open(file_path, 'r') as file:
		return read_in_ascii_format(file)

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
			elif bit == '\n':
				continue
			else:
				del epsilon[:]
				if len(bit) == 1:
					# Read an illegal character except '0', '1' or '\n'.
					return {'error': 101}
				else:
					# Lack of data to read.
					return {'error': 102}
			if  j == length:
				break
		test_suite()
		del epsilon[:]
	results_of_p_value_distribution()
	results_of_pass_rate()
	return {'success': 0}

def test_suite():
	length = get_value('length')
	is_selected = get_value('is_selected')
	block_length_of_frequency_within_a_block = get_value('block_length_of_frequency_within_a_block')
	if is_selected['frequencyTest']:
		frequency(length)
	if is_selected['frequencyTestWithinABlock']:
		frequency_within_a_block(block_length_of_frequency_within_a_block, length)
	if is_selected['runsTest']:
		runs(length)
	if is_selected['longestRunOfOnes']:
		longest_run_of_ones(length)

def results_of_p_value_distribution():
	amount = get_value('amount')
	p_value_dict = get_value('p_value_dict')
	p_value_distribution = get_value('p_value_distribution')
	for key in p_value_dict:
		if len(p_value_dict[key]):
			for i in range(len(p_value_dict[key])):
				index = int(p_value_dict[key][i] * 10)
				if index == 10:
					index -= 1
				p_value_distribution[key][index] += 1
			chi_squared = 0
			expected = amount / 10.0
			for i in range(10):
				chi_squared += ((p_value_distribution[key][i] - expected) ** 2) / expected
			p_value_distribution[key][10] = gammaincc(9.0 / 2.0, chi_squared / 2.0)
		else:
			p_value_distribution[key][10] = 0.0

def results_of_pass_rate():
	amount = get_value('amount')
	alpha = get_value('alpha')
	p_value_dict = get_value('p_value_dict')
	pass_rate = get_value('pass_rate')
	confidence_interval = get_value('confidence_interval')
	confidence_interval['confidence_level'] = 1 - alpha
	confidence_interval['general_interval'] = 3 * ((alpha * (1 - alpha) / amount) ** 0.5)
	for key in p_value_dict:
		count = 0
		for i in range(len(p_value_dict[key])):
			if p_value_dict[key][i] >= alpha:
				count += 1
			pass_rate[key] = float(count) / amount

def reset_results():
	reset_p_value_dict(get_value('p_value_dict'))
	reset_p_value_distribution(get_value('p_value_distribution'))
	reset_pass_rate(get_value('pass_rate'))
	reset_confidence_interval(get_value('confidence_interval'))

def reset_p_value_dict(d):
	for key in d:
		del d[key][:]

def reset_p_value_distribution(d):
	for key in d:
		d[key] = [0 for i in range(11)]

def reset_pass_rate(d):
	for key in d:
		d[key] = 0.0

def reset_confidence_interval(d):
	for key in d:
		d[key] = 0.0