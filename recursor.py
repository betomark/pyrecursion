# -*- coding: utf-8 -*-
from ast import literal_eval
from copy import copy

class recursion():
    def __init__(self, recursion_term_init, base_cases, recursive_step_function):
		"""
		This function will return recursive computation output
		"""
		self.r_t_init = recursion_term_init
		self.is_decreasing = True
	    self.last_base_case = []
		for i in base_cases:
			self.last_base_case.append(i)
			exec("self.res{} = {}".format(i, base_cases[i]))
		execution_order = generate_function_variables(recursive_step_function)
		if is_decreasing:
			execution_order.reverse()
		for result_index in execution_order:
			exec("self.res{}".format(result_index))
		return exec("self.res{}".format(recursion_term_init))
	
	def purge_not_needed_results(self, i):
		"""
		This function it's just for clean resutls dictionary which will not be needed for further computations steps
		"""
		exec("del self.res{}".format(i))
	
	def generate_function_dictionary(self, r_s_function):
		"""
		This function will generate all needed function hierarchy in a dictionay,
		indexed by integer numbers in increasing index depending on their order of computation
		"""
		def next_step_update(terms_update):
			terms_update = [update(terms_update[i]) for i, update in enumerate(terms_update)]
			return terms_update
			
		def extract_terms_update(r_s_function):
			terms_update = []
			split = copy(r_s_functions).split('[').split(']')
			next_is_term_updater = False
			for function_slice in split:
				if next_is_term_updater:
					updater = lambda x: literal_eval(function_sice.replace('x', '{}').format(x))
					terms_update.append(updater)
					next_is_term_updater = False
					r_s_function.replace('[' + function_slice + ']', 'self.res[{}]')
					r_s_function.replace('x', '{variable}')
					if updater(self.r_t_init) < updater(updater(self.r_t_init)):
						self.is_decreasing = False
				else:
					if '[' in function_slice:
						next_is_term_updater = True
			return terms_update

		terms_update = extract_terms_update(r_s_function)
		index = 1
		next_terms = [update(self.r_t_init) for update in terms_update]
		res_index = self.r_t_init
		order = []
		self.last_base_case = min(self.last_base_case) if self.is_decreasing else max(self.last_base_case)
		while min(next_terms) >= self.last_base_case if self.is_decreasing else max(next_terms) <= self.last_base_case:
			order.append(res_index)
			exec("self.res{} = r_s_function.format(variable=res_index).format(*next_terms) ".format(res_index))
			terms_update = next_step_update(terms_update, self.r_t_init)
			res_index = min(next_terms) if self.is_decreasing else max(next_terms)
			next_terms = [update(self.r_t_init) for update in terms_update]
			index += 1
		return order
