# Assignment 3 - Ghostbusters

## Overview

This assignment introduces **probabilistic inference** in the context of a modified Pacman game called **Ghostbusters**. The objective is to track and hunt **invisible ghosts**
using **sensor observations** and **Bayesian reasoning**. You will implement belief updates, observation handling, and action selection for Pacman.

## Problem Description

Pacman is equipped with **sonar-like sensors** that provide **noisy distance readings** to ghosts. Using this sensory data and movement models, your task is to implement agents
that:

- Track the **probable positions** of ghosts over time.
- **Update beliefs** based on observations and ghost movement patterns.
- Implement a **greedy strategy** to chase ghosts based on most likely positions.

### Key Concepts:

- **Discrete distributions** over grid positions
- **Bayesian filtering** (observation updates and time elapse)
- **Greedy decision-making** using belief distributions
- **Handling uncertainty and noise**

## Tasks

The project is divided into five questions:

### Q1: DiscreteDistribution Class

Implement:

- `normalize()`: Normalizes values to sum to 1.
- `sample()`: Samples keys proportionally to their values.

### Q2: Observation Probability

Implement:

- `getObservationProb()`: Computes `P(observation | ghostPos, pacmanPos)` using `busters.getObservationProbability()` and handles special **jail cases**.

### Q3: Exact Inference (Observation Update)

Implement:

- `observeUpdate()`: Applies **Bayes’ rule** to update the belief distribution using the latest sensor reading.

### Q4: Exact Inference (Time Elapse)

Implement:

- `elapseTime()`: Predicts ghost movements using the **transition model** and updates beliefs over time.

### Q5: Greedy Ghost Hunting

Implement:

- `chooseAction()`: In `GreedyBustersAgent`, select the action that moves Pacman closer to the **most likely ghost**.

## Implementation Details

### Files to Edit

- `bustersAgents.py`: For Q5
- `solutions.py`: For Q1–Q4

### Files Provided (Do Not Modify)

- `inference.py`, `busters.py`, `game.py`, `util.py`, etc.

### Tests

Run tests with:

```bash
python autograder.py -q q1          # Run test for question 1
python autograder.py -q q2          # ...and so on
python autograder.py -q q3 --no-graphics  # Faster testing
```

Or run a specific test:

```bash
python autograder.py -t test_cases/q2/1-ObsProb
```

## Software Setup

### Prerequisites

- **Python 3**
- **Pacman project files** (provided in the starter zip)
- **No extra libraries required**
- **Do not use `random.choices()`**, as it's forbidden

### Running the Game

Play manually with:

```bash
python busters.py
```

Run autograded solutions:

```bash
python autograder.py -q q5
```

## Submission Instructions

1. Complete implementations in:
    - `bustersAgents.py`
    - `solutions.py`
2. Create a short **contributions document** (PDF, TXT, or DOCX) with team member roles.
3. Zip the following:
    - `bustersAgents.py`
    - `solutions.py`
    - `report.pdf` (or equivalent)
4. Submit the `.zip` to **OnQ** before the deadline.

## Grading Breakdown

| Component                   | Weight |
|-----------------------------|--------|
| Q1: DiscreteDistribution    | 0.5%   |
| Q2: Observation Prob.       | 0.5%   |
| Q3: Observation Update      | 0.5%   |
| Q4: Time Elapse             | 0.5%   |
| Q5: Greedy Action Selection | 0.5%   |
| Code Quality & Comments     | 0.5%   |
| **Total**                   | 3.0%   |

## Tips

- Watch the belief clouds converge while running graphics mode.
- Use `--no-graphics` for faster tests.
- Don’t forget to handle **jail states** in your probability logic!
- Always normalize distributions before using them for sampling or inference.

## Resources

- [Pacman AI Projects - UC Berkeley](http://ai.berkeley.edu/project_overview.html)
- Review `inference.py` for helper classes and context
- Ask TAs or check Piazza for clarifications
