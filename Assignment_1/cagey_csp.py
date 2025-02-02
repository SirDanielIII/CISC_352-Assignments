# =============================
# Student Names: Daniel Zhuo, Daniel Frankel, Max Godovanny
# Group ID: 31
# Date: 2025-02-02
# =============================
# CISC 352 - W23
# cagey_csp.py
# desc:
#

#Look for #IMPLEMENT tags in this file.
"""
All models need to return a CSP object, and a list of lists of Variable objects
representing the board. The returned list of lists is used to access the
solution.

For example, after these three lines of code

    csp, var_array = binary_ne_grid(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array is a list of all Variables in the given csp. If you are returning an entire grid's worth of Variables
they should be arranged linearly, where index 0 represents the top left grid cell, index n-1 represents
the top right grid cell, and index (n^2)-1 represents the bottom right grid cell. Any additional Variables you use
should fall after that (i.e., the cage operand variables, if required).

1. binary_ne_grid (worth 0.25/3 marks)
    - A model of a Cagey grid (without cage constraints) built using only
      binary not-equal constraints for both the row and column constraints.

2. nary_ad_grid (worth 0.25/3 marks)
    - A model of a Cagey grid (without cage constraints) built using only n-ary
      all-different constraints for both the row and column constraints.

3. cagey_csp_model (worth 0.5/3 marks)
    - a model of a Cagey grid built using your choice of (1) binary not-equal, or
      (2) n-ary all-different constraints for the grid, together with Cagey cage
      constraints.


Cagey Grids are addressed as follows (top number represents how the grid cells are addressed in grid definition tuple);
(bottom number represents where the cell would fall in the var_array):
+-------+-------+-------+-------+
|  1,1  |  1,2  |  ...  |  1,n  |
|       |       |       |       |
|   0   |   1   |       |  n-1  |
+-------+-------+-------+-------+
|  2,1  |  2,2  |  ...  |  2,n  |
|       |       |       |       |
|   n   |  n+1  |       | 2n-1  |
+-------+-------+-------+-------+
|  ...  |  ...  |  ...  |  ...  |
|       |       |       |       |
|       |       |       |       |
+-------+-------+-------+-------+
|  n,1  |  n,2  |  ...  |  n,n  |
|       |       |       |       |
|n^2-n-1| n^2-n |       | n^2-1 |
+-------+-------+-------+-------+

Boards are given in the following format:
(n, [cages])

n - is the size of the grid,
cages - is a list of tuples defining all cage constraints on a given grid.


each cage has the following structure
(v, [c1, c2, ..., cm], op)

v - the value of the cage.
[c1, c2, ..., cm] - is a list containing the address of each grid-cell which goes into the cage (e.g [(1,2), (1,1)])
op - a flag containing the operation used in the cage (None if unknown)
      - '+' for addition
      - '-' for subtraction
      - '*' for multiplication
      - '/' for division
      - '?' for unknown/no operation given

An example of a 3x3 puzzle would be defined as:
(3, [(3,[(1,1), (2,1)],"+"),(1, [(1,2)], '?'), (8, [(1,3), (2,3), (2,2)], "+"), (3, [(3,1)], '?'), (3, [(3,2), (3,3)], "+")])

"""
import itertools
from math import prod

from cspbase import *


def binary_ne_grid(cagey_grid):
    ##IMPLEMENT
    n = cagey_grid[0]  # Grid size is from the first element in cagey_grid
    csp = CSP("Cagey_Grid-BinaryNE")
    # Create 2D list storing variables for each cell in the (n x n) grid, with each of the domains being {1, 2, ..., n}.
    grid_vars = [[Variable(f'{i + 1},{j + 1}', list(range(1, n + 1))) for j in range(n)] for i in range(n)]
    # Add variables into the CSP
    for row in grid_vars:
        for variable in row:
            csp.add_var(variable)
    # Add the binary not-equal constraints for rows
    for i in range(n):
        for j in range(n):
            for k in range(j + 1, n):  # Need to do this to ensure unique values in each row
                c = Constraint(f"NotEqual_Row{i + 1},{j + 1})-({i + 1},{k + 1})", [grid_vars[i][j], grid_vars[i][k]])
                # Generate all possible pairs (a, b) where a and b are in {1, ..., n},
                # and only include pairs where a != b, which ensures that two cells in the same row cannot have the same value.
                c.add_satisfying_tuples([(a, b) for a in range(1, n + 1) for b in range(1, n + 1) if a != b])
                csp.add_constraint(c)
    # Add binary not-equal constraints for columns
    for j in range(n):
        for i in range(n):
            for k in range(i + 1, n):  # Need to do this to ensure unique values in each column
                c = Constraint(f'NotEqual_Column({i + 1},{j + 1})-({k + 1},{j + 1})', [grid_vars[i][j], grid_vars[k][j]])
                # Generate all possible pairs (a, b) where a and b are in {1, ..., n},
                # and only include pairs where a != b, which ensures that two cells in the same column cannot have the same value.
                c.add_satisfying_tuples([(a, b) for a in range(1, n + 1) for b in range(1, n + 1) if a != b])
                csp.add_constraint(c)
    return csp, grid_vars

def nary_ad_grid(cagey_grid):
    ## IMPLEMENT
    n = cagey_grid[0]  # Grid size is from the first element in cagey_grid
    csp = CSP("Cagey_Grid-NaryAllDiff")
    # Create 2D list storing variables for each cell in the (n x n) grid, with each of the domains being {1, 2, ..., n}.
    grid_vars = [[Variable(f'{i + 1},{j + 1}', list(range(1, n + 1))) for j in range(n)] for i in range(n)]
    # Add variables into the CSP
    for row in grid_vars:
        for variable in row:
            csp.add_var(variable)
    # Add n-ary all-different constraints for rows
    for i in range(n):
        row = grid_vars[i]
        c = Constraint(f"AllDiff_Row({i + 1})", row)
        # Generate all possible permutations (a, b) where a and b are in {1, ..., n}
        c.add_satisfying_tuples([tup for tup in itertools.permutations(range(1, n + 1), n)])
        csp.add_constraint(c)
    # Add n-ary all-different constraints for columns
    for j in range(n):
        column = [grid_vars[i][j] for i in range(n)]
        c = Constraint(f'AllDiff_Column({j + 1})', column)
        # Generate all possible permutations (a, b) where a and b are in {1, ..., n}
        satisfying_tuples = [tup for tup in itertools.permutations(range(1, n + 1), n)]
        c.add_satisfying_tuples(satisfying_tuples)
        csp.add_constraint(c)
    return csp, grid_vars

def cagey_csp_model(cagey_grid):
    ##IMPLEMENT
    n, cages = cagey_grid  # Extract grid size and cages
    csp = CSP("Cagey_Grid-CSP")
    # Create 2D list storing variables for each cell in the (n x n) grid, with each of the domains being {1, 2, ..., n}.
    grid_vars = [[Variable(f'{i + 1},{j + 1}', list(range(1, n + 1))) for j in range(n)] for i in range(n)]
    # Add variables into the CSP
    for row in grid_vars:
        for variable in row:
            csp.add_var(variable)
    # Add row/column uniqueness using n-ary all-different
    for i in range(n):
        row = grid_vars[i]
        column = [grid_vars[j][i] for j in range(n)]
        csp.add_constraint(Constraint(f'AllDiff_Row({i + 1})', row))
        csp.add_constraint(Constraint(f'AllDiff_Column({i + 1})', column))
    # Flatten so far
    var_array = [v for row in grid_vars for v in row]
    for value, cells, operator in cages:
        # Assign domain for cage variable
        if operator is None or operator == '?':
            op_domain = ['+', '-', '*', '/']
            op_str = '?'
        else:
            op_domain = [operator]
            op_str = operator
        # We want something like "Cage_op(6:+:[Var-Cell(1,1), Var-Cell(1,2), Var-Cell(2,1), Var-Cell(2,2)])"
        cell_names_str = ", ".join(f"Var-Cell({r},{c})" for (r, c) in cells)
        cage_var_name = f"Cage_op({value}:{op_str}:[{cell_names_str}])"
        cage_var = Variable(cage_var_name, op_domain)
        csp.add_var(cage_var)
        var_array.append(cage_var)
        # Build the scope: [cage_var] + the cell variables
        cage_cells = [grid_vars[r - 1][c - 1] for (r, c) in cells]  # -1 for zero-based indexing (cages are one-based indexing)
        scope = [cage_var] + cage_cells
        # Build the Constraint
        con = Constraint(f"Cage({cells})", scope)
        # Generate satisfying tuples
        valid_tuples = []
        combos = itertools.product(*[v.domain() for v in cage_cells])  # The asterisk * unpacks the list of lists into separate arguments
        for combo in combos:
            for op in op_domain:
                k = len(combo)
                if op == '+':
                    if sum(combo) == value:
                        valid_tuples.append((op,) + combo)
                elif op == '*':
                    if prod(combo) == value:
                        valid_tuples.append((op,) + combo)
                elif op == '-':
                    if k == 2:  # 2-cell only
                        if abs(combo[0] - combo[1]) == value:
                            valid_tuples.append((op,) + combo)
                elif op == '/':
                    if k == 2:  # 2-cell only
                        x1, x2 = combo
                        if x2 != 0 and (x1 / x2) == value:
                            valid_tuples.append((op, x1, x2))
                        elif x1 != 0 and (x2 / x1) == value:
                            valid_tuples.append((op, x1, x2))
        con.add_satisfying_tuples(valid_tuples)
        csp.add_constraint(con)
    return csp, var_array
