#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def _init():
	global _global_dict
	_global_dict = {
		'amount': 0, 
		'length': 0,
		'epsilon': [],
		'p_value_dict' : {
			'frequency': []
		},
		'is_selected': {}
	}

def set_value(key,value):
	_global_dict[key] = value

def get_value(key):
	return _global_dict[key]