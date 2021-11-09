class Chess:
    def __init__(
                self, boardContent=None, boardInterface=None,
                gameFormat=None, timerFormat=None):
        self.boardContent = boardContent
        self.boardInterface = boardInterface
        self.gameFormat = gameFormat
        self.timerFormat = timerFormat
        self.lnmc = {
            'a': {
                1:self.boardContent[0][0],
                2:self.boardContent[0][1],
                3:self.boardContent[0][2],
                4:self.boardContent[0][3],
                5:self.boardContent[0][4],
                6:self.boardContent[0][5],
                7:self.boardContent[0][6],
                8:self.boardContent[0][7],
            },
            'b': {
                1:self.boardContent[1][0],
                2:self.boardContent[1][1],
                3:self.boardContent[1][2],
                4:self.boardContent[1][3],
                5:self.boardContent[1][4],
                6:self.boardContent[1][5],
                7:self.boardContent[1][6],
                8:self.boardContent[1][7],
            },
            'c': {
                1:self.boardContent[2][0],
                2:self.boardContent[2][1],
                3:self.boardContent[2][2],
                4:self.boardContent[2][3],
                5:self.boardContent[2][4],
                6:self.boardContent[2][5],
                7:self.boardContent[2][6],
                8:self.boardContent[2][7],
            },
            'd': {
                1:self.boardContent[3][0],
                2:self.boardContent[3][1],
                3:self.boardContent[3][2],
                4:self.boardContent[3][3],
                5:self.boardContent[3][4],
                6:self.boardContent[3][5],
                7:self.boardContent[3][6],
                8:self.boardContent[3][7],
            },
            'e': {
                1:self.boardContent[4][0],
                2:self.boardContent[4][1],
                3:self.boardContent[4][2],
                4:self.boardContent[4][3],
                5:self.boardContent[4][4],
                6:self.boardContent[4][5],
                7:self.boardContent[4][6],
                8:self.boardContent[4][7],
            },
            'f': {
                1:self.boardContent[5][0],
                2:self.boardContent[5][1],
                3:self.boardContent[5][2],
                4:self.boardContent[5][3],
                5:self.boardContent[5][4],
                6:self.boardContent[5][5],
                7:self.boardContent[5][6],
                8:self.boardContent[5][7],
            },
            'g': {
                1:self.boardContent[6][0],
                2:self.boardContent[6][1],
                3:self.boardContent[6][2],
                4:self.boardContent[6][3],
                5:self.boardContent[6][4],
                6:self.boardContent[6][5],
                7:self.boardContent[6][6],
                8:self.boardContent[6][7],
            },
            'h': {
                1:self.boardContent[7][0],
                2:self.boardContent[7][1],
                3:self.boardContent[7][2],
                4:self.boardContent[7][3],
                5:self.boardContent[7][4],
                6:self.boardContent[7][5],
                7:self.boardContent[7][6],
                8:self.boardContent[7][7],
            },
        }

    def start_game(self):
        self.board = Board()

# Piece color correspondance : 0 = blacks, 1 = whites
# Declaring players and which pieces they control, with the whites controlling
#   player starting.
        current_player = 0
        player1 = Player(color=1)
        player2 = Player(color=0)
#       self.boardinterface.mainloop()

# Dictionnary of chess coordinates to matrix coodinates
# Letters : x axis (a1 = [0][0], h1 = [7][0])
# Numbers : y axis (a1 = [0][0], a8 = [0][7])
    def l_n_m_c(self, letter, number):
        return self.lnmc[letter][number]

    def check_square(self):
        return None


class Player(Chess):
    def __init__(self, color=-1, timer=-1):
        self.color = color
# Intended for timer dependant game, might be reworked
        self.timer = timer


class Board(Chess):
    def __init__(self, boardContent=None, boardInterface=None):
        super.__init__(self)

    def init_board(self):
        board_array = []

        for length in range(8):
            length_array = []

            for width in range(8):
                length_array.append(None)

            board_array.append(length_array)

# This board piece initialisation is highly unsatifying, might be reworked
        # White and Black Rooks
        board_array[0][0] = Rook(False, '\u265C', 0)
        board_array[0][-1] = Rook(False, '\u265C', 0)
        board_array[-1][0] = Rook(False, '\u2656', 1)
        board_array[-1][-1] = Rook(False, '\u2656', 1)

        # White and Black Knights
        board_array[0][1] = Knight(False, '\u265E', 0)
        board_array[0][-2] = Knight(False, '\u265E', 0)
        board_array[-1][1] = Knight(False, '\u2658', 1)
        board_array[-1][-2] = Knight(False, '\u2658', 1)

        # White and black Bishops
        board_array[0][2] = Bishop(False, '\u265D', 0)
        board_array[0][-3] = Bishop(False, '\u265D', 0)
        board_array[-1][2]= Bishop(False, '\u2657', 1)
        board_array[-1][-3]= Bishop(False, '\u2657', 1)

        board_array[-1][-4]= King(False, '\u2654', 0)
        board_array[0][3]= Queen(False, '\u265B', 1)

        board_array[-1][-5] = Queen(False, '\u2655', 0)
        board_array[0][4] = King(False, '\u265A', 1)

        for i in range(8):
            board_array[1][i] = Pawn(False, '\u265F', 0)
            board_array[-2][i] = Pawn(False, '\u2659', 1)

        self.BoardContent = board_array

        return self.BoardContent


class Piece(Chess):
    def __init__(self, has_moved = False, symbol = "X", color = -1):
        self.has_moved = has_moved
        self.symbol = symbol
        self.color = color

    # Move
        # if piece passes through a piece, ally or enemy = illegal
            # That check doesn't apply to knights
        # if piece goes somewhere that's not allowed by
        # the piece pattern = illegal
        # if legal move ends on an enemy piece = enemy piece considered taken
        # and put aside

        #? () Interface : Display legal moves and takes by color

    def move_piece(self, letter, number, available_positions):
        if self.l_n_m_c(letter, number) not in available_positions:
            return "This piece cannot be moved here."
        elif self.l_n_m_c(letter, number) in available_positions:
            if type(self.l_n_m_c(letter, number)) != None:
                self.l_n_m_c(letter, number)
        if not self.has_moved:
            self.has_moved = True

class King(Piece):
    # Move pattern : [i][i+1], [i+1][i], [i+1][i+1], [i-1][i+1],
    # [i+1][i-1], [i-1][i], [i][i-1], [i-1][i-1]
    def __init__(
                self, has_moved = False, 
                symbol = "X", color = -1):
        super().__init__(has_moved, symbol, color)

class Rook(Piece):
    # Move pattern : [i][]
    def __init__(
                self, has_moved = False, 
                symbol = "X", color = -1):
        super().__init__(has_moved, symbol, color)

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol

class Bishop(Piece):
    def __init__(
                self, has_moved = False, 
                symbol = "X", color = -1):
        super().__init__(has_moved, symbol, color)

class Queen(Piece):
    def __init__(
                self, has_moved = False, 
                symbol = "X", color = -1):
        super().__init__(has_moved, symbol, color)

class Knight(Piece):
    def __init__(
                self, has_moved = False, 
                symbol = "X", color = -1):
        super().__init__(has_moved, symbol, color)

class Pawn(Piece):
    def __init__(
                self, has_moved = False, 
                symbol = "X", color = -1):
        super().__init__(has_moved, symbol, color)

def main():
    game = Chess()
    game.start_game()

if __name__ == "__main__":
    main()