# search.py
# ---------
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

'''
    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
            For a given state, this should return a list of triples, (successor,
            action, stepCost), where 'successor' is a successor to the current
            state, 'action' is the action required to get there, and 'stepCost'
            is the incremental cost of expanding to that successor
        """

        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            # Add a successor state to the successor list if the action is legal
            # Here's a code snippet for figuring out whether a new position hits a wall:
            x,y = state
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            hitsWall = self.walls[nextx][nexty]

            if not hitsWall:
                nextState = (nextx, nexty)
                # Check if it hits a corner
                corners_list = []

                if nextState in self.corners and nextState not in self.corners_hit:

                    self.corners_hit.add(nextState)
                    for entries in nextState:
                        corners_list.append(entries)
                else:
                    corners_list = state[1]

                corners_tuple = tuple(corners_list)
                successors.append(((nextx, nexty),corners_tuple), action)

        self._expanded += 1 # DO NOT CHANGE


        return successors


'''

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """

    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"




    South = Directions.SOUTH
    West = Directions.WEST
    North = Directions.NORTH
    East = Directions.EAST

    dis_set = set()
    fringe = util.Stack()
    initial_data = [problem.getStartState(), [], 0]




    fringe.push(initial_data)

    while not fringe.isEmpty(): # This implies that no solution was found.

        node = fringe.pop()

        if problem.isGoalState(node[0]):
            print(len(node[1]))
            return node[1] # This would give the path to follow

        if node[0] not in dis_set:
            dis_set.add(node[0])
            for child in problem.getSuccessors(node[0]):

                point = child[0]
                direction = []
                for value in node[1]:
                    direction.append(value)
                direction.append(child[1])
                fringe_data = [point, direction, 0]
                fringe.push(fringe_data)






def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""



    South = Directions.SOUTH
    West = Directions.WEST
    North = Directions.NORTH
    East = Directions.EAST

    dis_set = set()
    fringe = util.Queue()
    initial_data = [problem.getStartState(), []]

    fringe.push(initial_data)

    while not fringe.isEmpty():  # This implies that no solution was found.

        node = fringe.pop()

        if problem.isGoalState(node[0]):
            print(len(node[1]))
            return node[1]  # This would give the path to follow

        if node[0] not in dis_set:
            dis_set.add(node[0])
            for child in problem.getSuccessors(node[0]):

                point = child[0]
                direction = []
                for value in node[1]:
                    direction.append(value)
                direction.append(child[1])
                fringe_data = [point, direction]
                fringe.push(fringe_data)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    South = Directions.SOUTH
    West = Directions.WEST
    North = Directions.NORTH
    East = Directions.EAST

    dis_set = set()
    fringe = util.PriorityQueue()
    initial_data = [problem.getStartState(), [], 0]

    fringe.push(initial_data, 0)

    while not fringe.isEmpty():  # This implies that no solution was found.

        node = fringe.pop() # lowest priority node

        if problem.isGoalState(node[0]):
            return node[1]  # This would give the path to follow

        if node[0] not in dis_set:
            dis_set.add(node[0])
            for child in problem.getSuccessors(node[0]):

                point = child[0]
                direction = []
                priority = child[2] + node[2]
                for value in node[1]:
                    direction.append(value)
                direction.append(child[1])
                fringe_data = [point, direction, priority]
                fringe.push(fringe_data, priority)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    print('hello')
    print(problem.getStartState())


    South = Directions.SOUTH
    West = Directions.WEST
    North = Directions.NORTH
    East = Directions.EAST

    dis_set = set()
    fringe = util.PriorityQueue()
    initial_data = [problem.getStartState(), [], 0]

    fringe.push(initial_data, 0)

    while not fringe.isEmpty():  # This implies that no solution was found.

        node = fringe.pop() # lowest priority node

        if problem.isGoalState(node[0]):
            return node[1]  # This would give the path to follow

        if node[0] not in dis_set:
            dis_set.add(node[0])
            for child in problem.getSuccessors(node[0]):

                point = child[0]
                direction = []
                priority = child[2] + node[2]
                for value in node[1]:
                    direction.append(value)
                direction.append(child[1])
                fringe_data = [point, direction, priority]
                fringe.push(fringe_data, priority + heuristic(child[0],problem))





# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
