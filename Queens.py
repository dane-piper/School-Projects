#  File: Queens.py

#  Description: Solves and prints all the solutions to the queens problem given the board dimensions

#  Student Name: Dane Piper

#  Student UT EID: dap3498

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 3/13/2020

#  Date Last Modified: 3/13/2020

class Queens(object):
    # initialize the board
    def __init__(self, n=8):
        self.count = 0
        self.valid = 0
        self.board = []
        self.n = n
        self.queens = 0
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()

    # check if no queen captures another
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do a recursive backtracking solution
    def recursive_solve(self, col):
        if (col == self.n):
            return True
        else:
            for i in range(self.n):
                if (self.is_valid(i, col)):
                    self.board[i][col] = 'Q'
                    self.queens += 1
                    if self.recursive_solve(col + 1) and self.queens == self.n:
                        self.print_board()
                        print('')
                        self.count += 1
                    self.board[i][col] = '*'
                    self.queens -= 1
            return self.count

    # if the problem has a solution print the board
    def solve(self):
        for i in range(self.n):
            self.recursive_solve(i)


def main():
    # create a regular chess board
    size = 0
    while size > 8 or size < 1:
        size = int(input('Enter the size of board: '))
        print('')
    game = Queens(size)
    # place the queens on the board
    game.solve()
    print('There are {count} solutions for a {n} x {n} board.'.format(count=game.count, n=size))


main()
