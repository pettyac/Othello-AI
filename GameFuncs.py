import copy

from SearchNode import SearchNode

N, NE, E, SE, S, SW, W, NW = [-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]
DIRS = [N, NE, E, SE, S, SW, W, NW]
BOARD_SIZE = 4

## TEST VALIDITY
#   returns TRUE if the attempted move is a legal othello move
#   moves are valid if the placed piece results in at least
#   1 flip of an opponents piece. No scoring checks are made here
##
def test_validity(home, node, player):
    opponent = 'B' if player == 'W' else 'W'
    for dx, dy in DIRS:
        (x, y) = home[0] + dx, home[1] + dy
        if (not in_bounds(x, y)) or (node.state[x][y] != opponent):
            continue

        while ((in_bounds(x + dx, y + dy)) and (node.state[x][y] == opponent)):
            x, y = (x + dx), (y + dy)
            if node.state[x][y] == player:
                return True
    return False
            

## IN BOUNDS
#   keeps moves from happening off the board
##
def in_bounds(x, y):
    if (x < 0) or (x >= BOARD_SIZE) or (y < 0) or (y >= BOARD_SIZE):
        return False
    else: return True


## FLIP LOCATIONS
#   Takes a already established valid move and returns
#   a list of the (x, y) of each piece taken in the move
##
def flip_locations(state, home, player):
    opponent = 'B' if player == 'W' else 'W'
    flips = []
    ## step in each direction from the home location
    for dx, dy in DIRS:
        x, y = home
        x += dx
        y += dy
        ## ignore invalid paths
        if (not in_bounds(x, y)) or (state[x][y] != opponent):
            continue
        ## keep stepping if pieces are being flipped while staying in bounds
        while (state[x][y] == opponent and (in_bounds(x + dx, y + dy))):
            # if next step is a players piece, stop and record the steps 
            if state[x + dx][y + dy] == player:
                # backtrack to starting point and add flipped pieces coords to list
                while ((x, y) != home):
                    flips.append((x, y))
                    x -= dx
                    y -= dy 
                break
            else:
                x += dx
                y += dy
    return flips


## APPLY ACTION
#   Returns the new game board (state) after commiting
#   to an already established valid move 
##  
def apply_action(state, action, player):
    x, y = action 
    flips = flip_locations(state, action, player)
    state[x][y] = player
    for flip in flips:
        x, y = flip
        state[x][y] = player
    return state

# wrapper function for creating children
def create_child(node, state, action):
    node.insert(SearchNode(state, action))


## GET VALID MOVES
#   Takes a search node as an input and creates 
#   child nodes for each possible move that can
#   be made from the current game state
def get_valid_moves(node, player):
    opponent ='W' if player  == 'B' else 'B'

    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if node.state[x][y] != ' ': continue    ## Skip over the space if it isn't blank
            
            valid = test_validity((x, y), node, player)
            if valid:
                state = copy.deepcopy(node.state)
                state = apply_action(state, (x, y), player)
                create_child(node, state, (x, y))


## SCORE STATE
# Analyzes and returns the margin of victory for 
# any given game state. Players piece add 1 to the
# score while opponent pieces subtract 1 from the score
##
def score_state(state, player):
    opponent = 'W' if player == 'B' else 'B'
    score = 0
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if state[x][y] == ' ':
                continue
            elif state[x][y] == player:
                score += 1
            else: # opponent piece
                score -= 1    
    return score       


# Prints the game board
def print_board(board_state):
    for row in board_state:
        print row
