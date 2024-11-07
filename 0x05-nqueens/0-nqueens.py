#!/usr/bin/python3
'''
N-Queens Challenge

This program solves the N-Queens problem, where the goal
is to place N queens on an N×N chessboard
such that no two queens threaten each other.
A queen can attack another queen if they share the
same row, column, or diagonal.

Usage:
    $ python3 nqueens.py N

Where:
    N (integer) is the size of the chessboard and the
    number of queens to place. The program will attempt to
    find all valid solutions where no two queens attack each other.

    - N must be an integer greater than or equal to 4.
    The N-Queens problem has no solution for
      values of N less than 4.

The solution prints all possible valid solutions in a list
format. Each solution is represented
as a list of coordinate pairs [row, column], where a queen
is placed at the corresponding (row, column) position.

Example:
    $ python3 nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]

This script uses a backtracking algorithm to explore
possible placements of queens row by row,
pruning invalid configurations as it goes.

'''

import sys

if __name__ == '__main__':
    # Ensure correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Try to convert the input argument to an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    # Validate that N is at least 4
    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    placed_queens = []
    stop = False
    r = 0  # Starting row
    c = 0  # Starting column

    # Backtracking algorithm to solve the N-Queens problem
    while r < n:
        goback = False

        # Iterate through columns to try placing a queen
        while c < n:
            safe = True
            for cord in placed_queens:
                col = cord[1]

                if (col == c or col + (r-cord[0]) == c or
                        col - (r-cord[0]) == c):
                    safe = False
                    break

            if not safe:
                if c == n - 1:
                    goback = True
                    break
                c += 1
                continue

            # Place queen at the current position
            cords = [r, c]
            placed_queens.append(cords)

            # If last row is reached, store the solution
            if r == n - 1:
                solutions.append(placed_queens[:])

                for cord in placed_queens:
                    if cord[1] < n - 1:
                        r = cord[0]
                        c = cord[1]
                for i in range(n - r):
                    placed_queens.pop()
                if r == n - 1 and c == n - 1:
                    placed_queens = []
                    stop = True
                r -= 1
                c += 1
            else:
                c = 0
            break

        if stop:
            break

        # Backtrack if no valid placement is found in the current row
        if goback:
            r -= 1
            while r >= 0:
                c = placed_queens[r][1] + 1
                del placed_queens[r]  # Remove the last placed queen
                if c < n:
                    break
                r -= 1
            if r < 0:
                break
            continue
        r += 1

    # Print the list of solutions
    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
