"""
Apple Game Experiment 1:
How much of the board can be cleared by brute force?

The game itself is at: https://en.gamesaien.com/game/fruit_box/
"""

import random
from apple_functions import print_board, clear_p_by_q


def main():
    """Perform experiment 1."""
    m = 10  # Number of rows
    n = 17  # Number of columns

    # Board is a 2d list of random integers between 1 and 9
    board = [[random.randint(1, 9) for _ in range(n)] for _ in range(m)]
    print("Initial board:")
    print_board(board)

    # For every box size, clear all of those sized boxes that can be cleared
    # Do this process twice
    for k in range(2):
        for i in range(1, n):
            for j in range(1, m):
                clear_p_by_q(board, i, j)

    print("\nFinal board:")
    print_board(board)


if __name__ == '__main__':
    main()
