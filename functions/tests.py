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
	set_value('finished_tests_num', get_value('finished_tests_num') + 1)

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
	set_value('finished_tests_num', get_value('finished_tests_num') + 1)

def runs(n):
	epsilon = get_value('epsilon')
	p_value_dict = get_value('p_value_dict')
	summary = 0
	for i in range(n):
		summary += epsilon[i]
	pi = float(summary) / n
	if abs(pi - 0.5) > (2 / sqrt(n)):
		p_value = 0.0
	else:
		r_obs = 1
		for i in range(1, n):
			if epsilon[i] != epsilon[i - 1]:
				r_obs += 1
		p_value = erfc(abs(r_obs - 2 * n * pi * (1 - pi)) / (2 * sqrt(2 * n) * pi * (1 - pi)))
	p_value_dict['runs'].append(p_value)
	set_value('finished_tests_num', get_value('finished_tests_num') + 1)

def longest_run_of_ones(n):
	epsilon = get_value('epsilon')
	p_value_dict = get_value('p_value_dict')
	if n < 128:
		p_value = 0.0
	else:
		if n < 6272:
			K = 3
			M = 8
			V = (1, 2, 3, 4)
			pi = (0.2148, 0.3672, 0.2305, 0.1875)
		elif n < 750000:
			K = 5
			M = 128
			V = (4, 5, 6, 7, 8, 9)
			pi = (0.1174, 0.2430, 0.2493, 0.1752, 0.1027, 0.1124)
		else:
			K = 6
			M = 10000
			V = (10, 11, 12, 13, 14, 15, 16)
			pi = (0.0882, 0.2092, 0.2483, 0.1933, 0.1208, 0.0675, 0.0727)
		length_of_a_block = n / M
		v = [0, 0, 0, 0, 0, 0, 0]
		for i in range(length_of_a_block):
			v_obs = 0
			run = 0
			for j in range(M):
				if epsilon[i * M + j] == 1:
					run += 1
					v_obs = run if run > v_obs else v_obs
				else:
					run = 0
			if v_obs <= V[0]:
				v[0] += 1
			for j in range(1, K):
				if v_obs == V[j]:
					v[j] += 1
			if v_obs >= V[K]:
				v[K] += 1
		chi_squared = 0
		for i in range(K + 1):
			chi_squared += ((v[i] - length_of_a_block * pi[i]) ** 2) / (length_of_a_block * pi[i])
		p_value = gammaincc(K / 2.0, chi_squared / 2.0)
	p_value_dict['longest_run_of_ones'].append(p_value)
	set_value('finished_tests_num', get_value('finished_tests_num') + 1)