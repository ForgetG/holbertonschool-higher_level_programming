#!/usr/bin/python3
'''Program to resolve the N queens problem'''

import sys


def is_safe(board, row, col, n):
    '''Checks if it's safe to place a queen at board[row][col]

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index.
        col (int): The column index.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    '''
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n, solutions):
    '''Solves the N queens problem using backtracking

    Args:
        board (list): The current state of the chessboard.
        col (int): The current column index.
        n (int): The size of the chessboard.
        solutions (list): A list to store the solutions.

    Returns:
        None
    '''
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, n, solutions)
            board[i][col] = 0


def solve_n_queens(n):
    '''Initializes the chessboard and starts the solving process

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A list of solutions,
            where each solution is a list of queen positions.
    '''
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)
