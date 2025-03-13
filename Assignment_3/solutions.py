# solutions.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

'''Implement the methods from the classes in inference.py here'''

import util
from util import raiseNotDefined
import random
import busters

def normalize(self):
    """
    Normalize the distribution such that the total value of all keys sums
    to 1. The ratio of values for all keys will remain the same. In the case
    where the total value of the distribution is 0, do nothing.

    >>> dist = DiscreteDistribution()
    >>> dist['a'] = 1
    >>> dist['b'] = 2
    >>> dist['c'] = 2
    >>> dist['d'] = 0
    >>> dist.normalize()
    >>> list(sorted(dist.items()))
    [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0)]
    >>> dist['e'] = 4
    >>> list(sorted(dist.items()))
    [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0), ('e', 4)]
    >>> empty = DiscreteDistribution()
    >>> empty.normalize()
    >>> empty
    {}
    """
    "*** YOUR CODE HERE ***"
    total_sum = sum(self.values()) # calculate sum of distribution values
    if total_sum == 0: # Do nothing if sum is 0
        return
    
    # Convert keys to list to avoid modifying the dictionary
    keys = list(self.keys())
    for key in keys:
        self[key] /= total_sum  # normalize by dividing each key by the total sum
    #raiseNotDefined()

def sample(self):
    """
    Draw a random sample from the distribution and return the key, weighted
    by the values associated with each key.

    >>> dist = DiscreteDistribution()
    >>> dist['a'] = 1
    >>> dist['b'] = 2
    >>> dist['c'] = 2
    >>> dist['d'] = 0
    >>> N = 100000.0
    >>> samples = [dist.sample() for _ in range(int(N))]
    >>> round(samples.count('a') * 1.0/N, 1)  # proportion of 'a'
    0.2
    >>> round(samples.count('b') * 1.0/N, 1)
    0.4
    >>> round(samples.count('c') * 1.0/N, 1)
    0.4
    >>> round(samples.count('d') * 1.0/N, 1)
    0.0
    """
    "*** YOUR CODE HERE ***"
    total = sum(self.values()) # sums up all values in distribution
    
    threshold = random.random() * total # randomly creates a threshold
    sum_prob = 0 # tracks the total probability
    
    for key, value in self.items(): # loops through distribution and adds probabilities unitl threshold is reached and current key is returned
        sum_prob += value
        if sum_prob >= threshold:
            return key

    #raiseNotDefined()


def getObservationProb(self, noisyDistance, pacmanPosition, ghostPosition, jailPosition):
    """
    Return the probability P(noisyDistance | pacmanPosition, ghostPosition).
    """
    "*** YOUR CODE HERE ***"
    if ghostPosition == jailPosition:# Special case for if the ghost is in jail
        if noisyDistance is None: # returns 1 if obervation is None, and 0 probability with everything else 
            return 1
        return 0
    
    if noisyDistance is None: # if the ghost is not in jail but the observation distance is 0, returns 0
        return 0
    
    trueDistance = util.manhattanDistance(pacmanPosition, ghostPosition) # gets true distance between pacman and ghost using mahnattanDistance from util.py
    return busters.getObservationProbability(noisyDistance, trueDistance) # returns observation probability using the observation distance and true distance
    #raiseNotDefined()



def observeUpdate(self, observation, gameState):
    """
    Update beliefs based on the distance observation and Pacman's position.

    The observation is the noisy Manhattan distance to the ghost you are
    tracking.

    self.allPositions is a list of the possible ghost positions, including
    the jail position. You should only consider positions that are in
    self.allPositions.

    The update model is not entirely stationary: it may depend on Pacman's
    current position. However, this is not a problem, as Pacman's current
    position is known.
    """
    "*** YOUR CODE HERE ***"
    """
    Update beliefs based on the distance observation and Pacman's position.
    """
    pacmanPosition = gameState.getPacmanPosition() # gets Pacman pos
    jailPosition = self.getJailPosition() # gets jail pos
    newBeliefs = util.Counter() # to store new belif values

    for position in self.allPositions:
        probability = self.getObservationProb(observation, pacmanPosition, position, jailPosition) # Get the observation probability of each position
        newBeliefs[position] = self.beliefs.get(position, 0) * probability  # gets the current belief for each position
    
    # If the observation is None, the ghost is in jail
    if observation is None:
        newBeliefs = util.Counter()  # Reset all beliefs
        newBeliefs[jailPosition] = 1.0  # Place the new belief of the Pacman in jail
    
    # Normalize beliefs to create a proper probability distribution
    total = sum(newBeliefs.values())
    for position in newBeliefs:
        newBeliefs[position] /= total

    self.beliefs = newBeliefs  # Store the updated beliefs


def elapseTime(self, gameState):
    """
    Predict beliefs in response to a time step passing from the current
    state.

    The transition model is not entirely stationary: it may depend on
    Pacman's current position. However, this is not a problem, as Pacman's
    current position is known.
    """
    "*** YOUR CODE HERE ***"
    #raiseNotDefined()
    """
    Predict beliefs in response to a time step passing from the current state.
    """
    newBeliefs = util.Counter()  # created to store new belif values
    
    for oldPos in self.allPositions: # iterate through every psoition possible before current moment
        newPosDist = self.getPositionDistribution(gameState, oldPos)  # returns distribution over where the ghost might move to
        for newPos, prob in newPosDist.items(): # iterate over the new positions where ghost can be
            newBeliefs[newPos] += self.beliefs.get(oldPos, 0) * prob  # gets the current belief for each position
    
    # Normalize beliefs to create a proper probability distribution
    total = sum(newBeliefs.values())
    for position in newBeliefs:
        newBeliefs[position] /= total

    self.beliefs = newBeliefs # stores the updated beleifs