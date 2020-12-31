N, NE, E, SE, S, SW, W, NW = [-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]
DIRS = [N, NE, E, SE, S, SW, W, NW]

moves = {}

def get_move(board_size, board_state, turn, time_left, opponent_time_left):
    moves.clear()
    best = 0
    for x in range(board_size):
        for y in range(board_size):
            if board_state[x][y] != ' ':
                continue
            opp_pieces = test_move(x, y, board_state, board_size, turn) 
            if opp_pieces:
                moves[(x, y)] = opp_pieces
                if len(opp_pieces) > best:
                    best = len(opp_pieces)
                    X, Y = x, y
    if moves: return [X, Y]

    else: return None


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


def print_board(board_state):
    for row in board_state:
        print row


def apply_action(board_state, action, turn):
    x, y = action
    board_state[x][y] = turn
    for piece in moves[(x, y)]:
        x, y = piece
        board_state[x][y] = turn
    return board_state


if __name__ == "__main__":
    ## Replace with whatever board size you want to run on
    board_state = [[' ', ' ', ' ', ' '],
                   [' ', 'W', 'B', ' '],
                   [' ', 'B', 'W', ' '],
                   [' ', ' ', ' ', ' ']]
    board_size = 4
