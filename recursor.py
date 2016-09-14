# -*- coding: utf-8 -*-
from ast import literal_eval
from copy import copy

def recursor(recursion_term_init, base_cases, recursive_step_function):
	"""
	This function will return recursive computation output
	"""
	results_dictionary = base_cases
	function_dictionary = generate_function_dictionary(recursion_term_init, recursive_step_function)
	for function_index in map(lambda x: x+1, range(max(function_dictionary.keys()).reverse()):
		results_dictionary[] = function_dictionary[function_index]  # TODO: results_dictionary index
	return results_dictionary[recursion_term_init]


def purge_not_needed_results():
	"""
	This function it's just for clean resutls dictionary which will not be needed for further computations steps
	"""
	pass

def generate_function_dictionary(r_t_init, r_s_function):
	"""
	This function will generate all needed function hierarchy in a dictionay,
	indexed by integer numbers in increasing index depending on their order of computation
	"""
	def next_step_update(terms_update):
		return [update(terms_update[i]) for i, update in enumerate(terms_update)]
		
	def extract_terms_update(r_s_function):
		terms_update = []
		split = copy(r_s_functions).split('[').split(']')
		next_is_term_updater = False
		for function_slice in split:
			if next_is_term_updater:
				terms_update.append(lambda x: literal_eval(function_sice.replace('x', '{}').format(x)))
				next_is_term_updater = False
				r_s_function.replace('[' + function_slice + ']', 'results_dictionary[{}]')
			else:
				if '[' in function_slice:
					next_is_term_updater = True
		return terms_update
	
	terms_update = extract_terms_update(r_s_function)
	function_dictionary = {}
	index = 1
	next_terms = [update(r_t_init) for update in terms_update]
	while min(next_terms) > 0:
		function_dictionary[index] = r_s_function.format(*next_terms) 
		terms_update = next_step_update(terms_update)
		next_terms = [update(r_t_init) for update in terms_update]
		index += 1
	
	return function_dictionary
