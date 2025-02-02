# =============================
# Student Names: Daniel Zhuo, Daniel Frankel, Max Godovanny
# Group ID: 31
# Date: 2025-02-02
# =============================
# CISC 352 - W23
# heuristics.py
# desc:
#


#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

"""This file will contain different constraint propagators to be used within
   the propagators

1. ord_dh (worth 0.25/3 points)
    - a Variable ordering heuristic that chooses the next Variable to be assigned
      according to the Degree heuristic

2. ord_mv (worth 0.25/3 points)
    - a Variable ordering heuristic that chooses the next Variable to be assigned
      according to the Minimum-Remaining-Value heuristic


var_ordering == a function with the following template
    var_ordering(csp)
        ==> returns Variable

    csp is a CSP object---the heuristic can use this to get access to the
    Variables and constraints of the problem. The assigned Variables can be
    accessed via methods, the values assigned can also be accessed.

    var_ordering returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.
   """

def ord_dh(csp):
    """ return next Variable to be assigned according to the Degree Heuristic """
    # IMPLEMENT
    unassigned_variables = [variable for variable in csp.get_all_vars() if not variable.is_assigned()]
    # If there are no unassigned variables left, then return None.
    # If there are unassigned variables left, return the variable involved in the most constraints (most connected variable)
    return max(unassigned_variables, key=lambda var: len([c for c in csp.get_all_cons() if var in c.get_scope()])) if unassigned_variables else None

def ord_mrv(csp):
    """ return Variable to be assigned according to the Minimum Remaining Values heuristic """
    # IMPLEMENT
    unassigned_variables = [variable for variable in csp.get_all_vars() if not variable.is_assigned()]
    # If there are no unassigned variables left, then return None.
    # If there are unassigned variables left, return the one with the smallest domain size.
    # `key=lambda unassigned_var: unassigned_var.cur_domain_size()` tells min() to compare variables based on their cur_domain_size().
    return min(unassigned_variables, key=lambda var: var.cur_domain_size()) if unassigned_variables else None
