#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def global_variables_initialization():
	global _global_dict
	_global_dict = {
		'amount': 0, 
		'length': 0,
		'block_length_of_frequency_within_a_block': 0,
		'is_selected': {},
		'epsilon': [],
		'p_value_dict': {
			'frequency': [],
			'frequency_within_a_block': [],
			'runs': [],
			'longest_run_of_ones_in_a_block': []
		},
		'p_value_distribution': {
			'frequency': [0 for i in range(11)],
			'frequency_within_a_block': [0 for i in range(11)],
			'runs': [0 for i in range(11)],
			'longest_run_of_ones_in_a_block': [0 for i in range(11)]
		}
	}

def set_value(key, value):
	_global_dict[key] = value

def get_value(key):
	return _global_dict[key]