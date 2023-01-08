## Practice opponent bot. Makes a random choice of its valid moves

import random

from GameFuncs import BOARD_SIZE
from GameFuncs import test_validity

def get_move(node, player):
    moves = []
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if node.state[x][y] != ' ':
                continue
            valid = test_validity((x, y), node, player) 
            if valid:
                moves.append((x, y))

    if moves:
        i =  random.randrange(0,(len(moves)))
        return moves[i]
    else: return None


if __name__ == "__main__":
    pass