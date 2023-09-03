"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def actions(board):
    return {(i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell == EMPTY}


def result(board, action):
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action.")
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None

    # Max-Value helper function for X
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    # Min-Value helper function for O
    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    # Main logic for minimax
    current_player = player(board)
    best_value = float('-inf') if current_player == X else float('inf')
    best_action = None

    for action in actions(board):
        new_board = result(board, action)
        new_value = max_value(new_board) if current_player == X else min_value(new_board)

        if (current_player == X and new_value > best_value) or (current_player == O and new_value < best_value):
            best_value = new_value
            best_action = action

    return best_action
