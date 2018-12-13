#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from math import sqrt, erfc
from scipy.special import gammaincc
from functions.myglobals import *

def frequency(n):
	epsilon = get_value('epsilon')
	p_value_dict = get_value('p_value_dict')
	summary = 0
	for i in range(n):
		summary += 2 * epsilon[i] - 1
	s_obs = abs(summary) / sqrt(n)
	p_value = erfc(s_obs / sqrt(2))
	p_value_dict['frequency'].append(p_value)

def frequency_within_a_block(M, n):
	epsilon = get_value('epsilon')
	p_value_dict = get_value('p_value_dict')
	summary = 0
	length_of_a_block = n / M
	for i in range(length_of_a_block):
		summary_of_a_block = 0
		for j in range(M):
			summary_of_a_block += epsilon[i * M + j]
		pi = float(summary_of_a_block) / M
		v = pi - 0.5
		summary += v ** 2 
	chi_squared = 4 * M * summary
	p_value = gammaincc(length_of_a_block / 2.0, chi_squared / 2.0)
	p_value_dict['frequency_within_a_block'].append(p_value)