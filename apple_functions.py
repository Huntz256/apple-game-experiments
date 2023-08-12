"""
Utility functions for apple game experiments.
"""


def get_score(board):
    """Return the board's score (the number of "empty spaces," which are represented by zeros). """
    return sum(sum(1 for x in row if x == 0) for row in board)


def print_board(board):
    """Print the given board and its score."""
    for row in board:
        row2 = [x if x != 0 else ' ' for x in row]
        print(*row2)
    print("Score:", get_score(board))


def clear_pairs(board):
    """Clear all pairs in the given board."""
    m = len(board)  # Number of rows
    n = len(board[0])  # Number of columns
    for i in range(m):
        for j in range(n - 1):
            if board[i][j] + board[i][j + 1] == 10:
                board[i][j] = board[i][j + 1] = 0

    for j in range(n):
        for i in range(m - 1):
            if board[i][j] + board[i + 1][j] == 10:
                board[i][j] = board[i + 1][j] = 0


def clear_pairs_edges_first(board):
    """Clear all pairs in the given board, checking the edges of the board first and moving in towards the center.
    Assumes the board is of default size (10 rows, 17 columns). """

    # The 5 "outer rings" of the board, starting with the outermost
    for k in range(5):
        i = 0 + k
        for j in range(16):
            if board[i][j] + board[i][j + 1] == 10:
                board[i][j] = board[i][j + 1] = 0
            if board[i][j] + board[i + 1][j] == 10:
                board[i][j] = board[i + 1][j] = 0
        i = 9 - k
        for j in range(16):
            if board[i][j] + board[i][j + 1] == 10:
                board[i][j] = board[i][j + 1] = 0
            if board[i][j] + board[i - 1][j] == 10:
                board[i][j] = board[i - 1][j] = 0
        j = 0 + k
        for i in range(9):
            if board[i][j] + board[i + 1][j] == 10:
                board[i][j] = board[i + 1][j] = 0
            if board[i][j] + board[i][j + 1] == 10:
                board[i][j] = board[i][j + 1] = 0
        j = 16 - k
        for i in range(9):
            if board[i][j] + board[i + 1][j] == 10:
                board[i][j] = board[i + 1][j] = 0
            if board[i][j] + board[i][j - 1] == 10:
                board[i][j] = board[i][j - 1] = 0

    # The remainder of the board
    for k in range(5, 8):
        j = 0 + k
        for i in range(9):
            if board[i][j] + board[i + 1][j] == 10:
                board[i][j] = board[i + 1][j] = 0
            if board[i][j] + board[i][j + 1] == 10:
                board[i][j] = board[i][j + 1] = 0
        j = 16 - k
        for i in range(9):
            if board[i][j] + board[i + 1][j] == 10:
                board[i][j] = board[i + 1][j] = 0
            if board[i][j] + board[i][j - 1] == 10:
                board[i][j] = board[i][j - 1] = 0


def clear_p_by_q(board, p, q):
    """Clear all p by q sized boxes in the given board.

    Example 1.
    Given the board on the left, p = 1, q = 2, the result is the board on the right:
        0 0 3 7   ->   0 0 0 0
        5 5 0 3        0 0 0 3

    Example 2. p = 2, q = 2:
        4 1 0 5 0   ->   0 0 0 0 0
        0 5 0 0 5        0 0 0 0 0
    """
    m = len(board)     # Number of rows
    n = len(board[0])  # Number of columns

    for i in range(m - p + 1):
        for j in range(n - q + 1):
            total = sum(board[i + i2][j + j2] for j2 in range(q) for i2 in range(p))
            if total == 10:
                for i2 in range(p):
                    for j2 in range(q):
                        board[i + i2][j + j2] = 0
