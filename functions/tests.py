#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from math import sqrt, erfc
from functions.myglobals import *

def frequency(n):
	epsilon = get_value('epsilon')
	p_value_dict = get_value('p_value_dict')	
	sum = 0
	for i in range(n):
		sum += 2 * epsilon[i] - 1
	s_obs = abs(sum) / sqrt(n)
	f = s_obs / sqrt(2)
	p_value = erfc(f)
	p_value_dict['frequency'].append(p_value)