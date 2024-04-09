import chess


# This is fen analyzer takes in user fen spreads the board state into dirc vectors
# Analyze fen and output binary form of attack situation on board and its squares
# Author: Jalp


# general overview, keys are piece strings, value is binary form of attack from opposition
def get_normal_overview_of_board(board):#
    normal_overiew = {}
    for square in chess.SQUARES:
        p = board.piece_at(square)
        if p is not None:
            normal_overiew[str(p)] =int(board.is_attacked_by(not board.turn, square))

    return normal_overiew


# detailed overview, keys are piece strings, value is binary form of attack from opposition
# including all the pieces and its square number from 0 to 64 - 1

def get_spec_overview_of_board_with_sq_number(board):
    sq_count = {}
    for sq in chess.SQUARES:
        p = board.piece_at(sq)
        if p is not None:
            attk = int(board.is_attacked_by(not board.turn, sq))
            if str(p) not in sq_count:
                sq_count[str(p)] = []
            sq_count[str(p)].append((attk, sq))

    return sq_count


# create a board object for given FEN
def create_board_from_fen(fen):
    return chess.Board(fen)

# print the board
def print_board(board):
    print(board)


# driver code
def driver_code():
    fen = input("Pass in FEN: \n")
    custom_fen = "rnbqkbnr/ppp1pp1p/6p1/3p3Q/4P3/8/PPPP1PPP/RNB1KBNR w KQkq - 0 3"
    board = create_board_from_fen(fen)
    attacked_dict = get_normal_overview_of_board(board)
    attacked_info = get_spec_overview_of_board_with_sq_number(board)
    print_board(board)
    print("This is attacked vector on high level overview \n")
    print(attacked_dict)
    print("This is detailed attacked vector on specific sqs \n")
    print(attacked_info)

driver_code()


