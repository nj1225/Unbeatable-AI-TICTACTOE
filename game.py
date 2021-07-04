import time
#import math
from main import  GeniusComputerPlayer ,RandomComputerPlayer #HumanPlayer,


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # we wil use a single list to represent our 3*3 board
        self.current_winner = None  # keep track of the winner

    def print_board(self):

        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def print_board_nums():
        # 0|1|2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('|', '|'.join(row) + '|')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # OR,,,[ANOTHER WAY]
        # moves = []
        # for (i,spot) in enumerate(self.board):
        # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        # if spot == ' ' :
        # moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board  # will return boolean to tell whether or not there is empty spot on the board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move,then make amove [assign square to letter]
        # then return True,if invalid,return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere,we here to check all of this
        # first lets check the Rrow
        row_indented = square // 3
        row = self.board[row_indented * 3:  (row_indented + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check coloumn
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # check diagonal
        # but only if the square is an even number (0, 2 , 4 ,6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all of thses fails
        return False


def play(games, x_pla, o_pla, print_game=True):
    # returns the winner of the game(the letter).. OR none for a tie
    if print_game:
        games.print_board_nums()

    letter = 'x'  # starting letter
    # iterate while the game still has empty squares
    # (we do not have to worry about winner because we will just return that
    # which braks the loop)
    while games.empty_squares():
        # get the mive fromm the appropriate player
        if letter == 'o':
            square = o_pla.get_move(games)

        else:
            square = x_pla.get_move(games)

        # let define a function to make a move!!
        if games.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square{square}')
                games.print_board()
                print('')  # just an empty line

            if games.current_winner:
                # is not none
                if print_game:
                    print(letter + ' WINS!!!')
                return letter

                # after we made our move ,we need to alternate letters
            letter = 'o' if letter == 'x' else 'x'  # switching players

            # if letter == 'x'
            #   letter = 'o'
            # else:
            #   letter = 'x'

        # tiny break to make things a little bit easier to read
        if print_game:
            time.sleep(0.8)

    if print_game:
        print('It\'s a TIE')


if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(100):
        x_pla = RandomComputerPlayer('x')
        o_pla = GeniusComputerPlayer('o')
        t = TicTacToe()
        result = play(t, x_pla, o_pla, print_game=True)
        if result == 'x':
            x_wins += 1
        elif result == 'o':
            o_wins += 1
        else:
            ties +=1
    print(f'After a 100 iteration we can see that {x_wins} x_wins, {o_wins} o_wins and {ties} ties')