# -*- coding: utf-8 -*-
from ast import literal_eval
from copy import copy

class recursion():
    def __init__(self, recursion_term_init, base_cases, recursive_step_function): 
	"""
	This function will return recursive computation output
	"""
	for i in base_cases:
            exec("self.res{} = {}".format(i, base_cases[i]))
	generate_function_variables(recursion_term_init, recursive_step_function)
	for result_index in :
		exec("exec(self.res{})".format(result_index)
		
	return exec("self.res{}".format(recursion_term_init))

    
def purge_not_needed_results():
	"""
	This function it's just for clean resutls dictionary which will not be needed for further computations steps
	"""
	# exec("del self.res{}".format())
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
				r_s_function.replace('[' + function_slice + ']', 'res[{}]')
			else:
				if '[' in function_slice:
					next_is_term_updater = True
		return terms_update
	
	terms_update = extract_terms_update(r_s_function)
	index = 1
	next_terms = [update(r_t_init) for update in terms_update]
	while min(next_terms) > 0:
		exec("self.res{} = r_s_function.format(*next_terms) ".format())
		terms_update = next_step_update(terms_update)
		next_terms = [update(r_t_init) for update in terms_update]
		index += 1
	
