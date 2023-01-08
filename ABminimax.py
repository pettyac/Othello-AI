import copy

from SearchNode import SearchNode
from GameFuncs import *

INF = 100000000
nINF = -100000000


def get_move(node, player):
    x = ABsearch(node, player)
    for c in node.children:
        if x == c.util_value:
            return c.action

def ABsearch(node, player):
    opponent = 'W' if player == 'B' else 'B'
    MAX = max_value(node, nINF, INF, player, opponent)
    return MAX


def max_value(node, alpha, beta, player, opponent):

    get_valid_moves(node, player)
    if node.is_terminal():
        node.util_value = score_state(node.state, player)
        return node.util_value
    
    node.util_value = nINF
    for c in node.children:
        node.util_value = max(node.util_value, min_value(c, alpha, beta, player, opponent))
        if node.util_value >= beta:
            return node.util_value 
        alpha = max(alpha, node.util_value)
    return node.util_value 


def min_value(node, alpha, beta, player, opponent):
    
    get_valid_moves(node, opponent)
    if node.is_terminal():
        node.util_value = score_state(node.state, player)
        return node.util_value
    
    node.util_value = INF
    for c in node.children:
        node.util_value = min(node.util_value, max_value(c, alpha, beta, player, opponent))
        if node.util_value <= alpha:
            return node.util_value 
        beta = min(beta, node.util_value)
    return node.util_value 
 

if __name__ == '__main__':
    pass
