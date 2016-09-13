# -*- coding: utf-8 -*-

def recursor(recursion_term_init, base_cases, recursive_step_function, terms_update=[lambda x: x - 1], terms_operations=[]):
	"""
	This function will return recursive computation output
	"""
	results_dictionary = {i + 1: case for i, case in enumerate(base_cases)}
	function_dictionary = generate_function_dictionary(recursion_term_init, recursive_step_function, terms_update, terms_operations)

def store_function_result():
	"""
	This function will store a computed result of a recursive step
	"""
	pass

def purge_not_needed_results():
	"""
	This function it's just for clean resutls dictionary which will not be needed for further computations steps
	"""
	pass

def generate_function_dictionary(r_t_init, r_s_function, terms_update, terms_operations):
	"""
	This function will generate all needed function hierarchy in a dictionay,
	indexed by integer numbers in increasing index depending on their order of computation
	"""
	def next_step_update(terms_update):
		return [update(terms_update[i]) for i, update in enumerate(terms_update)]
		
	function_dictionary = {}
	index = 1
	next_terms = [update(r_t_init) for update in terms_update]
	while min(next_terms) > 0:
		'''
		dictionary construction
		'''
		terms_update = next_step_update(terms_update)
		next_terms = [update(r_t_init) for update in terms_update]
		index += 1
	return function_dictionary
