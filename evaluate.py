import random
import time

import chess


class Local_Board_random(chess.Board):  # sub classs which copy a chess.Board() object
    def __init__(self, board):
        super().__init__()
        fen_parts = board.fen().split()
        self.set_board_fen(fen_parts[0])
        self.turn = board.turn
        self.eval = 0
        self.ordered_moves = []
        self.evaluate()
        self.best_move()

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

    def best_move(self):  ## best move just one half move ahead
        all_moves_eval = []
        for try_move in self.legal_moves:
            # make the move
            self.push(try_move)
            # evaluate the board
            self.evaluate()
            # add the move and the evaluation to the list
            all_moves_eval.append((try_move, self.eval))
            # undo the move
            self.pop()
        # sort the list by the evaluation
        all_moves_eval.sort(key=lambda x: x[1], reverse=self.turn)
        print(list(all_moves_eval))
        all_moves_eval = list(all_moves_eval)
        random.shuffle(all_moves_eval)
        self.ordered_moves = all_moves_eval


class Local_Board_1a(chess.Board):  # sub classs which copy a chess.Board() object
    def __init__(self, board):
        super().__init__()
        fen_parts = board.fen().split()
        self.set_board_fen(fen_parts[0])
        self.turn = board.turn
        self.eval = 0
        self.ordered_moves = []
        self.evaluate()
        self.best_move()

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

    def best_move(self):  ## best move just one half move ahead
        all_moves_eval = []
        for try_move in self.legal_moves:
            # make the move
            self.push(try_move)
            # evaluate the board
            self.evaluate()
            # add the move and the evaluation to the list
            all_moves_eval.append((try_move, self.eval))
            # undo the move
            self.pop()
        # sort the list by the evaluation
        all_moves_eval.sort(key=lambda x: x[1], reverse=self.turn)
        print(list(all_moves_eval))
        self.ordered_moves = list(all_moves_eval)


### Ajout de la recherche a une profondeure de 2 coups

class Local_Board_2a(chess.Board):  # sub classs which copy a chess.Board() object
    def __init__(self, board):
        super().__init__()
        fen_parts = board.fen().split()
        self.set_board_fen(fen_parts[0])
        self.turn = board.turn
        self.eval = 0
        self.ordered_moves = []
        self.evaluate()
        self.best_move()

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

    def best_move(self):  ## best move just one half move ahead
        all_moves_eval = []
        for try_move in self.legal_moves:
            # make the move
            self.push(try_move)
            # evaluate the board
            self.evaluate()
            d1 = self.eval
            # do the same for opponent moves
            opponent_move = []
            for try_opponent_move in self.legal_moves:
                self.push(try_opponent_move)
                # evaluate the board
                self.evaluate()
                d2 = self.eval
                # create a list of oppenent moves and their evaluation
                opponent_move.append([try_opponent_move, d2])
                # undo the move
                self.pop()

            # sort the list by the evaluation
            opponent_move.sort(key=lambda x: x[1], reverse=False)

            # add the move and the evaluation to the list
            all_moves_eval.append((try_move, opponent_move[0][1]))

            # undo the move
            self.pop()

        # detect the best move

        # sort the list by the evaluation
        all_moves_eval.sort(key=lambda x: x[1], reverse=self.turn)
        print(list(all_moves_eval))
        self.ordered_moves = list(all_moves_eval)


### Ajout de la recherche a une profondeure de 5 coups (boucle pour pouvoir en faire plus)
class Local_Board_5a(chess.Board):  # sub classs which copy a chess.Board() object
    def __init__(self, board):
        super().__init__()
        fen_parts = board.fen().split()
        self.set_board_fen(fen_parts[0])
        self.turn = board.turn
        self.eval = 0
        self.ordered_moves = []
        self.evaluate()
        self.best_move_rec(3)

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

    def best_move(self):  ## best move just one half move ahead
        all_moves_eval = []
        for try_move in self.legal_moves:
            # make the move
            self.push(try_move)
            # evaluate the board
            self.evaluate()
            d1 = self.eval
            # do the same for opponent moves
            opponent_move = []
            for try_opponent_move in self.legal_moves:
                self.push(try_opponent_move)
                # evaluate the board
                self.evaluate()
                d2 = self.eval
                # create a list of oppenent moves and their evaluation
                opponent_move.append([try_opponent_move, d2])
                # undo the move
                self.pop()

            # sort the list by the evaluation
            opponent_move.sort(key=lambda x: x[1], reverse=False)

            # add the move and the evaluation to the list
            all_moves_eval.append((try_move, opponent_move[0][1]))

            # undo the move
            self.pop()

        # detect the best move

        # sort the list by the evaluation
        all_moves_eval.sort(key=lambda x: x[1], reverse=self.turn)
        print(list(all_moves_eval))
        self.ordered_moves = list(all_moves_eval)

    def best_move_rec(self, depth, alpha=-float('inf'), beta=float('inf')):
        if depth == 0:
            # if we've reached the maximum depth of recursion,
            # just evaluate the current board and return the result
            self.evaluate()
            return self.eval

        # initialize the list of possible moves and their evaluations
        possible_moves_eval = []

        # loop over all legal moves
        for try_move in self.legal_moves:
            # make the move
            self.push(try_move)

            # recursively evaluate the opponent's best response
            opponent_eval = self.best_move_rec(depth - 1)

            opponent_eval = self.best_move_rec(depth - 1, alpha, beta)

            # evaluate the current state of the board after the opponent's move
            self.evaluate()

            # calculate the total evaluation for this move by subtracting
            # the opponent's evaluation from our own
            total_eval = self.eval

            # add this move and its total evaluation to the list
            possible_moves_eval.append([try_move, total_eval])

            # undo the move
            self.pop()

            if self.turn == chess.WHITE:
                alpha = max(alpha, total_eval)
            else:
                beta = min(beta, total_eval)

                # check if we can prune the rest of the moves
            if alpha >= beta:
                break

        # choose the best move based on its total evaluation
        # sort list by evaluation
        possible_moves_eval.sort(key=lambda x: x[1], reverse=self.turn)
        self.ordered_moves = list(possible_moves_eval)


class Local_Board_5b(
    chess.Board):  # ajout de la notion de position sur l'echequier. controle du centre avec les pions, developpement des pieces, controle des cases autour du roi
    def __init__(self, board):
        super().__init__()
        fen_parts = board.fen().split()
        self.set_board_fen(fen_parts[0])
        self.turn = board.turn
        self.eval = 0
        self.ordered_moves = []
        self.evaluate()
        self.best_move_rec(3)

    def evaluate(self):
        piece_values = {
            chess.PAWN: 100,
            chess.ROOK: 500,
            chess.KNIGHT: 320,
            chess.BISHOP: 330,
            chess.QUEEN: 900,
            chess.KING: 20000
        }

        square_values = {1: 0.9, 2: 0.9, 3: 0.9, 4: 0.9, 5: 0.9, 6: 0.9, 7: 0.9, 8: 0.9,
                         9: 0.9, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 0.9,
                         17: 0.9, 18: 1.0, 19: 1.1, 20: 1.1, 21: 1.1, 22: 1.1, 23: 1.0, 24: 0.9,
                         25: 0.9, 26: 1.0, 27: 1.1, 28: 1.2, 29: 1.2, 30: 1.1, 31: 1.0, 32: 0.9,
                         33: 0.9, 34: 1.0, 35: 1.1, 36: 1.2, 37: 1.2, 38: 1.1, 39: 1.0, 40: 0.9,
                         41: 0.9, 42: 1.0, 43: 1.1, 44: 1.2, 45: 1.2, 46: 1.1, 47: 1.0, 48: 0.9,
                         49: 0.9, 50: 1.0, 51: 1.1, 52: 1.1, 53: 1.1, 54: 1.1, 55: 1.0, 56: 0.9,
                         57: 0.9, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 0.9}

        white_material = 0
        black_material = 0

        for square in chess.SQUARES:
            piece = self.piece_at(square)
            if not piece:
                continue
            if piece.color == chess.WHITE:
                white_material += piece_values[piece.piece_type]*square_values[square+1]
            else:
                black_material += piece_values[piece.piece_type]*square_values[square+1]

        self.eval = (white_material - black_material) / 100

    def best_move(self):  ## best move just one half move ahead
        all_moves_eval = []
        for try_move in self.legal_moves:
            # make the move
            self.push(try_move)
            # evaluate the board
            self.evaluate()
            d1 = self.eval
            # do the same for opponent moves
            opponent_move = []
            for try_opponent_move in self.legal_moves:
                self.push(try_opponent_move)
                # evaluate the board
                self.evaluate()
                d2 = self.eval
                # create a list of oppenent moves and their evaluation
                opponent_move.append([try_opponent_move, d2])
                # undo the move
                self.pop()

            # sort the list by the evaluation
            opponent_move.sort(key=lambda x: x[1], reverse=self.turn)

            # add the move and the evaluation to the list
            all_moves_eval.append((try_move, opponent_move[0][1]))

            # undo the move
            self.pop()

        # detect the best move

        # sort the list by the evaluation
        all_moves_eval.sort(key=lambda x: x[1], reverse=self.turn)
        print(list(all_moves_eval))
        self.ordered_moves = list(all_moves_eval)

    def best_move_rec(self, depth, alpha=-float('inf'), beta=float('inf')):
        if depth == 0:
            # if we've reached the maximum depth of recursion,
            # just evaluate the current board and return the result
            self.evaluate()
            return self.eval

        # initialize the list of possible moves and their evaluations
        possible_moves_eval = []

        # loop over all legal moves
        for try_move in self.legal_moves:
            # make the move
            self.push(try_move)

            # recursively evaluate the opponent's best response
            opponent_eval = self.best_move_rec(depth - 1)

            opponent_eval = self.best_move_rec(depth - 1, alpha, beta)

            # evaluate the current state of the board after the opponent's move
            self.evaluate()

            # calculate the total evaluation for this move by subtracting
            # the opponent's evaluation from our own
            total_eval = self.eval

            # add this move and its total evaluation to the list
            possible_moves_eval.append([try_move, total_eval])

            # undo the move
            self.pop()

            if self.turn == chess.WHITE:
                alpha = max(alpha, total_eval)
            else:
                beta = min(beta, total_eval)

                # check if we can prune the rest of the moves
            if alpha >= beta:
                break

        # choose the best move based on its total evaluation
        # sort list by evaluation
        possible_moves_eval.sort(key=lambda x: x[1], reverse=self.turn)
        self.ordered_moves = list(possible_moves_eval)
