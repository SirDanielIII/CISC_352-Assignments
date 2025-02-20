# Assignment 2 - The Treasure Hunter

## Overview

This assignment focuses on **planning and PDDL modeling**. The objective is to define a **PDDL domain** and implement several problem instances within that domain. The domain is
themed around a **treasure hunter navigating a dungeon**, unlocking doors, managing keys, and reaching a goal.

## Problem Description

A treasure hunter explores a **dungeon** that consists of **rooms and corridors**. The goal is to reach the **treasure room** while overcoming obstacles such as **locked corridors,
risky paths, and scattered keys**.

### Key Features of the Domain:

- The dungeon contains **rooms** connected by **corridors**.
- The hero can **move** between rooms via corridors unless they are **locked or collapsed**.
- Some corridors have **locks of different colors** that require keys.
- **Keys** can be **one-use, two-use, or multi-use**.
- Moving through **risky corridors** causes them to collapse and make the room **messy**.
- The hero can **pick up, drop, and use keys**, as well as **clean up messy rooms**.

### Actions the Hero Can Take:

1. **Move** to an adjacent room if the corridor is **not locked or collapsed**.
2. **Unlock** a locked corridor using the correct **colored key**.
3. **Pick up** a key if the hero is **not already holding one**.
4. **Drop** a key to leave it in the current room.
5. **Clean** a messy room.

## Implementation Details

### Files Included

- `domain.pddl`: Defines the **domain model** with **predicates, actions, and objects**.
- `problem1.pddl`: First predefined problem setup.
- `problem2.pddl`: Second predefined problem setup.
- `problem3.pddl`: Third predefined problem setup.
- `problem4.pddl`: A **custom problem** designed with extra constraints.

### Custom Problem Requirements

- The dungeon must contain **6-9 rooms**.
- The minimum number of **moves required must be greater than 20**.
- There must be **at least one locked corridor of every color**.

## Software Setup

### Prerequisites

- **PDDL Editor**: Use [Planning.Domains Editor](https://editor.planning.domains/) or **VS Code with PDDL extension**.
- **Planner**: You can use any compatible planner such as `Fast Downward` or `LPG`.

### Running the Code

1. Open the `.pddl` files in **Planning.Domains** or VS Code.
2. Load `domain.pddl` and select a **problem file**.
3. Run the planner to generate the solution plan.
4. Verify that the solution **successfully navigates** the dungeon and retrieves the **treasure**.

## Submission Instructions

- Package the following files into a `.zip` archive:
    - `domain.pddl`
    - `problem1.pddl`
    - `problem2.pddl`
    - `problem3.pddl`
    - `problem4.pddl`
    - `report.pdf` (contains team details and contributions)
- Submit the `.zip` file to **OnQ** before the deadline.

## Grading Breakdown

| Component                                               | Weight |
|---------------------------------------------------------|--------|
| Correct **domain encoding** (actions, predicates)       | 1.75%  |
| Correct **problem implementations** (1-3)               | 0.75%  |
| **Custom problem complexity**                           | 0.25%  |
| **Code readability (indentation, comments, structure)** | 0.25%  |
| **Total**                                               | 3%     |

## Additional Notes

- **Forbidden constructs**: Do not use `forall`, `exists`, `imply`, or `or`. You **can** use `not` and `and`.
- Ensure correct **naming conventions** for predicates and objects.
- Verify your PDDL models using **visualizations** before submission.

## Resources

- [PDDL Model Alignment Tutorial](https://editor.planning.domains/)
- [VS Code PDDL Plugin](https://marketplace.visualstudio.com/items?itemName=jan-dolejsi.pddl)

