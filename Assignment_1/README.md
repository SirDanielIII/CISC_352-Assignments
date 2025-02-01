# Assignment 1: Constraint Satisfaction Problems (CSPs)

## Overview

This assignment focuses on **Constraint Satisfaction Problems (CSPs)** and requires implementing:

- **Constraint Propagation Algorithms**: Forward Checking (FC) and Generalized Arc Consistency (GAC).
- **Variable Ordering Heuristics**: Minimum Remaining Value (MRV) and Degree Heuristic (DH).
- **CSP Models**: Three different Cagey puzzle models using binary and n-ary constraints.

## Tasks

1. Implement **propagators** for enforcing constraints during search.
2. Implement **heuristics** for improving search efficiency.
3. Build **CSP models** to solve an extended version of the Cagey puzzle.
4. Ensure your code passes the provided **autograder tests**.

## Software Setup

### Requirements

- **Python 3.5.2 or later** (ensure compatibility with testing environment)
- Standard Python libraries **(no external dependencies allowed)**
- Allowable built-in libraries:
    - `itertools` (`permutations`, `product`, `combinations`, etc.)
    - `math.prod`
    - `collections` (`deque`, `defaultdict`)
    - `operator.itemgetter`

### Running the Code

1. Download the starter files from the onQ page.
2. Implement the required functions in:
    - `propagators.py`
    - `heuristics.py`
    - `cagey_csp.py`
3. Run the **autograder** to validate your implementation:
   ```bash
   python3 autograder_stu.py
