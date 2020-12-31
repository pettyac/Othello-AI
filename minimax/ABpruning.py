import copy

INF = 100000000
nINF = -100000000

N, NE, E, SE, S, SW, W, NW = [-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]
DIRS = [N, NE, E, SE, S, SW, W, NW]
MOVES = {}


def test_move(x, y, board_state, board_size, turn):
    opponent = 'W' if turn == 'B' else 'B'
    player = turn
    start = (x, y)
    flips = []

    for dx, dy in DIRS:
        x, y = start 
        if not in_bounds(x+dx, y+dy, board_size):
            continue
        x, y = (x + dx), (y + dy)

        if board_state[x][y] != opponent:
            continue
        
        while ((in_bounds(x, y, board_size)) and board_state[x][y] == opponent):
            x, y = (x + dx), (y + dy)
            
            if not in_bounds(x, y, board_size) or board_state[x][y] != player:
                continue
            
            
            (x, y) = (x - dx), (y - dy) 
            while (x, y) != start:
                flips.append([x, y])
                x, y = (x - dx), (y - dy)

    return flips


def in_bounds(x, y, board_size):
    if (x >= 0) and (x < board_size):
        if (y >= 0) and (y < board_size):
            return True
    return False

def get_actions(board_state, board_size, turn):
    actions = []
    for x in range(board_size):
        for y in range(board_size):
            if board_state[x][y] != ' ':
                continue
            pieces = test_move(x, y, board_state, board_size, turn)
            if pieces:
                actions.append((x,y))
    return actions


def apply_action(board_state, board_size, action, turn):
    x, y = action
    flips = test_move(x, y, board_state, board_size, turn)
    board_state[x][y] = turn
    for flip in flips:
        x, y = flip
        board_state[x][y] = turn
    return board_state



def get_move(board_size, board_state, turn, time_left, opponent_time_left):
    if time_left > 150000:
        depth = 10
    elif time_left > 100000:
        depth = 20
    elif time_left > 50000:
        depth = 10
    else: depth = 8
    MOVES.clear()
    actions = []
    best = nINF
    for x in range(board_size):
        for y in range(board_size):
            if board_state[x][y] != ' ':
                continue
            opp_pieces = test_move(x, y, board_state, board_size, turn)
            if opp_pieces:
                MOVES[(x, y)] = opp_pieces
                actions.append((x,y))
    for action in actions:
        temp_board = apply_action(copy.deepcopy(board_state), board_size, action, turn)
        value = AlphaBeta_search(temp_board, board_size, turn, depth)
        if value >= best:
            best = value
            print value, action
            X, Y = action
    if MOVES: return [X, Y]
    else: return None


def score_state(board_state, board_size, player):
    opponent = 'W' if player == 'B' else 'B'
    score = 0
    for x in range(board_size):
        for y in range(board_size):
            if board_state[x][y] == ' ':
                continue
            elif board_state[x][y] == player:
                score += 1
            else: # opponent piece
                score -= 1    
    return score         
    

def AlphaBeta_search(board_state, board_size, player, depth):
    opponent = 'W' if player == 'B' else 'B'
    MAX = max_value(board_state, board_size, nINF, INF, player, opponent, depth)
    return MAX


def max_value(board_state, board_size, alpha, beta, player, opponent, depth):
    actions = []

    if depth == 0 or len(get_actions(board_state, board_size, player)) == 0:
        return score_state(board_state, board_size, player)

    v = nINF
    actions = get_actions(board_state, board_size, player)
    for action in actions:
        temp_board = apply_action(copy.deepcopy(board_state), board_size, action, player)
        v = max(v, min_value(temp_board, board_size, alpha, beta, opponent, player, depth - 1))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def min_value(board_state, board_size, alpha, beta, player, opponent, depth):
    actions = []
    if depth == 0 or len(get_actions(board_state, board_size, player)) == 0:
        return score_state(board_state, board_size, opponent) 
    v = INF
    actions = get_actions(copy.deepcopy(board_state), board_size, player)
    for action in actions:
        temp_board = apply_action(board_state, board_size, action, player)
        v = min(v, max_value(temp_board, board_size, alpha, beta, opponent, player, depth - 1))
        if v <= alpha:
             return v
        beta = min(beta, v)
    return v
 
if __name__ == '__main__':
    pass
