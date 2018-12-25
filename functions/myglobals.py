#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def global_variables_initialization():
	global _global_dict
	_global_dict = {
		'amount': 0, 
		'length': 0,
		'block_length_of_frequency_within_a_block': 0,
		'epsilon': [],
		'p_value_dict' : {
			'frequency': [],
			'frequency_within_a_block': [],
			'runs': [],
			'longest_run_of_ones_in_a_block': []
		},
		'is_selected': {}
	}

def set_value(key,value):
	_global_dict[key] = value

def get_value(key):
	return _global_dict[key]