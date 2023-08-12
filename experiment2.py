"""
Apple Game Experiment 2:
Is it better to start at the edges?
"""

import copy
import random
from apple_functions import get_score, clear_pairs, clear_pairs_edges_first, clear_p_by_q


def main():
    """Perform experiment 2."""
    m = 10  # Number of rows
    n = 17  # Number of columns

    alg1_scores = []
    alg2_scores = []

    for _ in range(100):
        board = [[random.randint(1, 9) for _ in range(n)] for _ in range(m)]
        board_copy = copy.deepcopy(board)

        clear_pairs_edges_first(board)
        for i in range(1, n):
            for j in range(1, m):
                clear_p_by_q(board, i, j)
        alg1_scores.append(get_score(board))

        clear_pairs(board_copy)
        for i in range(1, n):
            for j in range(1, m):
                clear_p_by_q(board_copy, i, j)
        alg2_scores.append(get_score(board_copy))
        print(end='.')

    print()
    print("Average alg1 (clear pairs in edges first) score:", sum(alg1_scores) / len(alg1_scores))
    print("Average alg2 score:", sum(alg2_scores) / len(alg2_scores))


if __name__ == '__main__':
    main()
