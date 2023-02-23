# interface du jeux d'échec

import chess
import random


class Board(chess.Board):  ### subclass of chess.board whith an eval function
    def __init__(self):
        chess.Board.__init__(self)
        self.eval = 0

    def evaluate(self):
        piece_values = {
            chess.PAWN: 100,
            chess.ROOK: 500,
            chess.KNIGHT: 320,
            chess.BISHOP: 330,
            chess.QUEEN: 900,
            chess.KING: 20000
        }

        white_material = 0
        black_material = 0

        for square in chess.SQUARES:
            piece = self.piece_at(square)
            if not piece:
                continue
            if piece.color == chess.WHITE:
                white_material += piece_values[piece.piece_type]
            else:
                black_material += piece_values[piece.piece_type]

        self.eval = (white_material - black_material) / 100


def get_move():
    print(Board.turn())
    move = input("Enter your move: ")
    return move


def do_move(move):
    Board.push(move)


def legal_moves():
    return list(Board.legal_moves)


def choice(list_of_moves):
    return random.choice(list_of_moves)


def best_move_1a(): ## best move just one half move ahead
    all_moves_eval = []

    for try_move in list(Board.legal_moves):  #### loop all move and look for the best eval after one move
        # make the move
        Board.push(try_move)
        # evaluate the board
        Board.evaluate()
        # add the move and the evaluation to the list
        all_moves_eval.append((try_move, Board.eval))
        # undo the move
        Board.pop()

    print(all_moves_eval)

    # sort the list by the evaluation
    all_moves_eval.sort(key=lambda x: x[1], reverse=True)
    print(all_moves_eval)
    print (all_moves_eval[0][0])
    print (all_moves_eval[0][1])
    return all_moves_eval[0][0]


Board = Board()


def game():
    white_brain = "best_move_1a"
    black_brain = "random"
    while not Board.is_game_over():
        #       if Board.turn() ## check if it's white turn (True) or black turn (False)

        print(Board)
        Board.evaluate()
        print(Board.eval)
        possible_moves = legal_moves()
        print(possible_moves)
        if Board.turn:  ## check if it's white turn (True) or black turn (False)
            best_move = best_move_1a()
            do_move(best_move)
        else:
            coup = choice(possible_moves)
            print(coup)
            do_move(coup)
