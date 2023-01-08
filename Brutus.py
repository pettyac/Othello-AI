## Practice opponent bot. Makes the most aggressive move each round
import copy

from GameFuncs import BOARD_SIZE
from GameFuncs import test_validity, apply_action, score_state

def get_move(node, player):
    moves = False
    best = -100
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if node.state[x][y] != ' ':
                continue
            valid = test_validity((x, y), node, player) 
            if valid:
                state = apply_action(copy.deepcopy(node.state), (x, y), player)
                hostility = score_state(state, player)
                if hostility > best:
                    (X, Y) = (x, y)
                    moves = True
    if moves:
        return (X, Y)
    else: return None


if __name__ == "__main__":
    pass