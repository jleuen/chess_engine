import random
import time
import json
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
                white_material += piece_values[piece.piece_type] * square_values[square + 1]
            else:
                black_material += piece_values[piece.piece_type] * square_values[square + 1]

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


class Local_Board_5c(chess.Board):  # ajout de la notion de position sur l'echequier. changement en fonction des pieces
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

        pawn_square_values = {1: 0.9, 2: 0.9, 3: 0.9, 4: 0.9, 5: 0.9, 6: 0.9, 7: 0.9, 8: 0.9,
                              9: 0.9, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 0.9,
                              17: 0.9, 18: 1.0, 19: 1.1, 20: 1.1, 21: 1.1, 22: 1.1, 23: 1.0, 24: 0.9,
                              25: 0.9, 26: 1.0, 27: 1.1, 28: 1.2, 29: 1.2, 30: 1.1, 31: 1.0, 32: 0.9,
                              33: 0.9, 34: 1.0, 35: 1.1, 36: 1.2, 37: 1.2, 38: 1.1, 39: 1.0, 40: 0.9,
                              41: 0.9, 42: 1.0, 43: 1.1, 44: 1.2, 45: 1.2, 46: 1.1, 47: 1.0, 48: 0.9,
                              49: 0.9, 50: 1.0, 51: 1.1, 52: 1.1, 53: 1.1, 54: 1.1, 55: 1.0, 56: 0.9,
                              57: 0.9, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 0.9}

        knight_square_values = pawn_square_values

        bishop_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                                9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                                17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                                25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                                33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                                41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                                49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                                57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        rook_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                              9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                              17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                              25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                              33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                              41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                              49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                              57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        queen_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                               9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                               17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                               25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                               33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                               41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                               49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                               57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        king_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                              9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                              17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                              25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                              33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                              41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                              49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                              57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        dict_of_square_values = {chess.PAWN: pawn_square_values, chess.KNIGHT: knight_square_values,
                                 chess.BISHOP: bishop_square_values, chess.ROOK: rook_square_values,
                                 chess.QUEEN: queen_square_values, chess.KING: king_square_values}

        white_material = 0
        black_material = 0

        for square in chess.SQUARES:
            piece = self.piece_at(square)
            if not piece:
                continue
            if piece.color == chess.WHITE:
                white_material += piece_values[piece.piece_type] * dict_of_square_values[piece.piece_type][square + 1]
            else:
                black_material += piece_values[piece.piece_type] * dict_of_square_values[piece.piece_type][square + 1]

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


class Local_Board_6c(chess.Board):  # change of the best_move_rec function to min max function from nadeem 4
    def __init__(self, board):
        super().__init__()
        fen_parts = board.fen().split()

        self.set_board_fen(fen_parts[0])
        self.turn = board.turn
        self.eval = 0
        self.ordered_moves = []
        self.evaluate()
        self.best_move = self.best_move_using_minmax(3, self.turn)

    def evaluate(self):
        piece_values = {
            chess.PAWN: 100,
            chess.ROOK: 500,
            chess.KNIGHT: 320,
            chess.BISHOP: 330,
            chess.QUEEN: 900,
            chess.KING: 20000
        }

        pawn_square_values = {1: 0.9, 2: 0.9, 3: 0.9, 4: 0.9, 5: 0.9, 6: 0.9, 7: 0.9, 8: 0.9,
                              9: 0.9, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 0.9,
                              17: 0.9, 18: 1.0, 19: 1.1, 20: 1.1, 21: 1.1, 22: 1.1, 23: 1.0, 24: 0.9,
                              25: 0.9, 26: 1.0, 27: 1.1, 28: 1.2, 29: 1.2, 30: 1.1, 31: 1.0, 32: 0.9,
                              33: 0.9, 34: 1.0, 35: 1.1, 36: 1.2, 37: 1.2, 38: 1.1, 39: 1.0, 40: 0.9,
                              41: 0.9, 42: 1.0, 43: 1.1, 44: 1.2, 45: 1.2, 46: 1.1, 47: 1.0, 48: 0.9,
                              49: 0.9, 50: 1.0, 51: 1.1, 52: 1.1, 53: 1.1, 54: 1.1, 55: 1.0, 56: 0.9,
                              57: 0.9, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 0.9}

        knight_square_values = pawn_square_values

        bishop_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                                9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                                17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                                25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                                33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                                41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                                49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                                57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        rook_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                              9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                              17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                              25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                              33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                              41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                              49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                              57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        queen_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                               9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                               17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                               25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                               33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                               41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                               49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                               57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        king_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                              9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                              17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                              25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                              33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                              41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                              49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                              57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        dict_of_square_values = {chess.PAWN: pawn_square_values, chess.KNIGHT: knight_square_values,
                                 chess.BISHOP: bishop_square_values, chess.ROOK: rook_square_values,
                                 chess.QUEEN: queen_square_values, chess.KING: king_square_values}

        white_material = 0
        black_material = 0

        for square in chess.SQUARES:
            piece = self.piece_at(square)
            if not piece:
                continue
            if piece.color == chess.WHITE:
                white_material += piece_values[piece.piece_type] * dict_of_square_values[piece.piece_type][square + 1]
            else:
                black_material += piece_values[piece.piece_type] * dict_of_square_values[piece.piece_type][square + 1]

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

    def minmax(self, max_depth, current_depth, is_max_player, nodes_per_depth):

        # This if else code block is only used for analysis of algorithm, by counting number of nodes explored
        if max_depth - current_depth in nodes_per_depth:
            nodes_per_depth[max_depth - current_depth] += 1
        else:
            nodes_per_depth[max_depth - current_depth] = 1

        # This is the base case, depth == 0 means it is a leaf node
        if current_depth == 0:
            self.evaluate()
            leaf_node_score = self.eval
            return leaf_node_score, nodes_per_depth

        if is_max_player:

            # set absurdly high negative value such that none of the static evaluation result less than this value
            best_score = -100000

            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))

                # pushing the current move to the board
                self.push(move)

                # calculating node score, if the current node will be the leaf node, then score will be calculated by static evaluation;
                # score will be calculated by finding max value between node score and current best score.
                node_score, nodes_per_depth = self.minmax(max_depth, current_depth - 1, False,
                                                          nodes_per_depth)

                # calculating the max value for the particular node
                best_score = max(best_score, node_score)

                # undoing the last move, so that we can evaluate next legal moves
                self.pop()

            return (best_score, nodes_per_depth)
        else:

            # set absurdly high positive value such that none of the static evaluation result more than this value
            best_score = 100000

            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))

                # pushing the current move to the board
                self.push(move)

                # calculating node score, if the current node will be the leaf node, then score will be calculated by static evaluation;
                # score will be calculated by finding min value between node score and current best score.
                node_score, nodes_per_depth = self.minmax(max_depth, current_depth - 1, True,
                                                          nodes_per_depth)

                # calculating the min value for the particular node
                best_score = min(best_score, node_score)

                # undoing the last move, so that we can evaluate next legal moves
                self.pop()

            return (best_score, nodes_per_depth)

    def best_move_using_minmax(self, depth, is_max_player):
        best_move_score = -1000000
        best_move = None

        nodes_per_depth = dict()

        for legal_move in self.legal_moves:
            move = chess.Move.from_uci(str(legal_move))
            self.push(move)
            move_score, nodes_per_depth = self.minmax(depth, depth, not self.turn, nodes_per_depth)
            score = max(best_move_score, move_score)
            self.pop()
            if score > best_move_score:
                best_move_score = score
                best_move = move
        print(best_move, nodes_per_depth)
        return (best_move, nodes_per_depth)

        # choose the best move based on its total evaluation
        # sort list by evaluation
        # possible_moves_eval.sort(key=lambda x: x[1], reverse=self.turn)
        # self.ordered_moves = list(possible_moves_eval)


class Local_Board_7c(chess.Board):  # add alpha beta purning
    def __init__(self, board):
        super().__init__()
        fen_parts = board.fen().split()

        self.set_board_fen(fen_parts[0])
        self.turn = board.turn
        self.eval = 0
        self.ordered_moves = []
        self.evaluate()
        self.best_move = self.best_move_using_minmax(5, self.turn)

    def evaluate(self):
        piece_values = {
            chess.PAWN: 100,
            chess.ROOK: 500,
            chess.KNIGHT: 320,
            chess.BISHOP: 330,
            chess.QUEEN: 900,
            chess.KING: 20000
        }

        pawn_square_values = {1: 0.9, 2: 0.9, 3: 0.9, 4: 0.9, 5: 0.9, 6: 0.9, 7: 0.9, 8: 0.9,
                              9: 0.9, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 0.9,
                              17: 0.9, 18: 1.0, 19: 1.1, 20: 1.1, 21: 1.1, 22: 1.1, 23: 1.0, 24: 0.9,
                              25: 0.9, 26: 1.0, 27: 1.1, 28: 1.2, 29: 1.2, 30: 1.1, 31: 1.0, 32: 0.9,
                              33: 0.9, 34: 1.0, 35: 1.1, 36: 1.2, 37: 1.2, 38: 1.1, 39: 1.0, 40: 0.9,
                              41: 0.9, 42: 1.0, 43: 1.1, 44: 1.2, 45: 1.2, 46: 1.1, 47: 1.0, 48: 0.9,
                              49: 0.9, 50: 1.0, 51: 1.1, 52: 1.1, 53: 1.1, 54: 1.1, 55: 1.0, 56: 0.9,
                              57: 0.9, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 0.9}

        knight_square_values = pawn_square_values

        bishop_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                                9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                                17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                                25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                                33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                                41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                                49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                                57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        rook_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                              9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                              17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                              25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                              33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                              41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                              49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                              57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        queen_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                               9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                               17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                               25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                               33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                               41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                               49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                               57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        king_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                              9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                              17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                              25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                              33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                              41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                              49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                              57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        dict_of_square_values = {chess.PAWN: pawn_square_values, chess.KNIGHT: knight_square_values,
                                 chess.BISHOP: bishop_square_values, chess.ROOK: rook_square_values,
                                 chess.QUEEN: queen_square_values, chess.KING: king_square_values}

        white_material = 0
        black_material = 0

        for square in chess.SQUARES:
            piece = self.piece_at(square)
            if not piece:
                continue
            if piece.color == chess.WHITE:
                white_material += piece_values[piece.piece_type] * dict_of_square_values[piece.piece_type][square + 1]
            else:
                black_material += piece_values[piece.piece_type] * dict_of_square_values[piece.piece_type][square + 1]

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

    def minmax(self, max_depth, current_depth, is_max_player, alpha, beta, nodes_per_depth):

        # This if else code block is only used for analysis of algorithm, by counting number of nodes explored
        if max_depth - current_depth in nodes_per_depth:
            nodes_per_depth[max_depth - current_depth] += 1
        else:
            nodes_per_depth[max_depth - current_depth] = 1

        # This is the base case, depth == 0 means it is a leaf node
        if current_depth == 0:
            self.evaluate()
            leaf_node_score = self.eval
            return leaf_node_score, nodes_per_depth

        if is_max_player:
            # set absurdly high negative value such that none of the static evaluation result less than this value
            best_score = -100000

            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))

                # pushing the current move to the board
                self.push(move)

                # calculating node score, if the current node will be the leaf node, then score will be calculated by static evaluation;
                # score will be calculated by finding max value between node score and current best score.
                node_score, nodes_per_depth = self.minmax(max_depth, current_depth - 1, False, alpha, beta,
                                                          nodes_per_depth)

                # calculating the max value for the particular node
                best_score = max(best_score, node_score)

                # undoing the last move, so that we can evaluate next legal moves
                self.pop()

                # alpha-beta pruning
                alpha = max(alpha, best_score)
                if alpha >= beta:
                    break

            return (best_score, nodes_per_depth)

        else:
            # set absurdly high positive value such that none of the static evaluation result more than this value
            best_score = 100000

            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))

                # pushing the current move to the board
                self.push(move)

                # calculating node score, if the current node will be the leaf node, then score will be calculated by static evaluation;
                # score will be calculated by finding min value between node score and current best score.
                node_score, nodes_per_depth = self.minmax(max_depth, current_depth - 1, True, alpha, beta,
                                                          nodes_per_depth)

                # calculating the min value for the particular node
                best_score = min(best_score, node_score)

                # undoing the last move, so that we can evaluate next legal moves
                self.pop()

                # alpha-beta pruning
                beta = min(beta, best_score)
                if alpha >= beta:
                    break

            return (best_score, nodes_per_depth)

    def best_move_using_minmax(self, depth, is_max_player):
        best_move_score = -1000000
        best_move = None

        nodes_per_depth = dict()

        for legal_move in self.legal_moves:
            move = chess.Move.from_uci(str(legal_move))
            self.push(move)
            move_score, nodes_per_depth = self.minmax(depth, depth, True, alpha=-float('inf'), beta=float('inf'),
                                                      nodes_per_depth=nodes_per_depth)
            score = max(best_move_score, move_score)
            self.pop()
            if score > best_move_score:
                best_move_score = score
                best_move = move
        print(best_move, nodes_per_depth)
        return (best_move, nodes_per_depth)

        # choose the best move based on its total evaluation
        # sort list by evaluation
        # possible_moves_eval.sort(key=lambda x: x[1], reverse=self.turn)
        # self.ordered_moves = list(possible_moves_eval)


class Local_Board_7d(chess.Board):  # add time management
    def __init__(self, board):
        super().__init__()
        fen_parts = board.fen().split()

        self.set_board_fen(fen_parts[0])
        self.turn = board.turn
        self.eval = 0
        self.ordered_moves = []
        self.evaluate()
        self.best_move = self.best_move_using_minmax(max_time=15, is_max_player=self.turn)

    def evaluate(self):
        piece_values = {
            chess.PAWN: 100,
            chess.ROOK: 500,
            chess.KNIGHT: 320,
            chess.BISHOP: 330,
            chess.QUEEN: 900,
            chess.KING: 20000
        }

        pawn_square_values = {1: 0.9, 2: 0.9, 3: 0.9, 4: 0.9, 5: 0.9, 6: 0.9, 7: 0.9, 8: 0.9,
                              9: 0.9, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 0.9,
                              17: 0.9, 18: 1.0, 19: 1.1, 20: 1.1, 21: 1.1, 22: 1.1, 23: 1.0, 24: 0.9,
                              25: 0.9, 26: 1.0, 27: 1.1, 28: 1.2, 29: 1.2, 30: 1.1, 31: 1.0, 32: 0.9,
                              33: 0.9, 34: 1.0, 35: 1.1, 36: 1.2, 37: 1.2, 38: 1.1, 39: 1.0, 40: 0.9,
                              41: 0.9, 42: 1.0, 43: 1.1, 44: 1.2, 45: 1.2, 46: 1.1, 47: 1.0, 48: 0.9,
                              49: 0.9, 50: 1.0, 51: 1.1, 52: 1.1, 53: 1.1, 54: 1.1, 55: 1.0, 56: 0.9,
                              57: 0.9, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 0.9}

        knight_square_values = pawn_square_values

        bishop_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                                9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                                17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                                25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                                33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                                41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                                49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                                57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        rook_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                              9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                              17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                              25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                              33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                              41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                              49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                              57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        queen_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                               9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                               17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                               25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                               33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                               41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                               49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                               57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        king_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                              9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                              17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                              25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                              33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                              41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                              49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                              57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        dict_of_square_values = {chess.PAWN: pawn_square_values, chess.KNIGHT: knight_square_values,
                                 chess.BISHOP: bishop_square_values, chess.ROOK: rook_square_values,
                                 chess.QUEEN: queen_square_values, chess.KING: king_square_values}

        white_material = 0
        black_material = 0

        for square in chess.SQUARES:
            piece = self.piece_at(square)
            if not piece:
                continue
            if piece.color == chess.WHITE:
                white_material += piece_values[piece.piece_type] * dict_of_square_values[piece.piece_type][square + 1]
            else:
                black_material += piece_values[piece.piece_type] * dict_of_square_values[piece.piece_type][square + 1]

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

    def minmax(self, max_depth, current_depth, is_max_player, alpha, beta, nodes_per_depth):

        # This if else code block is only used for analysis of algorithm, by counting number of nodes explored
        if max_depth - current_depth in nodes_per_depth:
            nodes_per_depth[max_depth - current_depth] += 1
        else:
            nodes_per_depth[max_depth - current_depth] = 1

        # This is the base case, depth == 0 means it is a leaf node
        if current_depth == 0:
            self.evaluate()
            leaf_node_score = self.eval
            return leaf_node_score, nodes_per_depth

        if is_max_player:
            # set absurdly high negative value such that none of the static evaluation result less than this value
            best_score = -100000

            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))

                # pushing the current move to the board
                self.push(move)

                # calculating node score, if the current node will be the leaf node, then score will be calculated by static evaluation;
                # score will be calculated by finding max value between node score and current best score.
                node_score, nodes_per_depth = self.minmax(max_depth, current_depth - 1, False, alpha, beta,
                                                          nodes_per_depth)

                # calculating the max value for the particular node
                best_score = max(best_score, node_score)

                # undoing the last move, so that we can evaluate next legal moves
                self.pop()

                # alpha-beta pruning
                alpha = max(alpha, best_score)
                if alpha >= beta:
                    break

            return (best_score, nodes_per_depth)

        else:
            # set absurdly high positive value such that none of the static evaluation result more than this value
            best_score = 100000

            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))

                # pushing the current move to the board
                self.push(move)

                # calculating node score, if the current node will be the leaf node, then score will be calculated by static evaluation;
                # score will be calculated by finding min value between node score and current best score.
                node_score, nodes_per_depth = self.minmax(max_depth, current_depth - 1, True, alpha, beta,
                                                          nodes_per_depth)

                # calculating the min value for the particular node
                best_score = min(best_score, node_score)

                # undoing the last move, so that we can evaluate next legal moves
                self.pop()

                # alpha-beta pruning
                beta = min(beta, best_score)
                if alpha >= beta:
                    break

            return (best_score, nodes_per_depth)

    def best_move_using_minmax(self, max_time, is_max_player):
        start_time = time.time()
        best_move_score = -1000000
        best_move = None
        nodes_per_depth = dict()

        # start with a depth limit of 1 and increment by 1 until the time limit is reached
        depth = 1
        while time.time() - start_time < max_time:
            print(depth)
            print(time.time() - start_time)
            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))
                self.push(move)
                move_score, nodes_per_depth = self.minmax(depth, depth, True, alpha=-float('inf'), beta=float('inf'),
                                                          nodes_per_depth=nodes_per_depth)
                score = max(best_move_score, move_score)
                self.pop()
                if score > best_move_score:
                    best_move_score = score
                    best_move = move
            depth += 1

        print(best_move, nodes_per_depth)
        return (best_move, nodes_per_depth)


class Local_Player_1a(chess.Board):  # add time management
    def __init__(self, board, color):
        super().__init__()
        fen_parts = board.fen().split()

        self.set_board_fen(fen_parts[0])
        self.turn = board.turn
        self.eval = 0
        self.ordered_moves = []
        self.evaluate()
        self.best_move = ""
        self.color = color

    def update(self, board):
        self.set_fen(board.fen())

    def choose_best_move(self):
        print("test")
        self.best_move = self.best_move_using_minmax(max_time=10, is_max_player=self.turn)
        print(self.best_move)

    def evaluate(self):
        piece_values = {
            chess.PAWN: 100,
            chess.ROOK: 500,
            chess.KNIGHT: 320,
            chess.BISHOP: 330,
            chess.QUEEN: 900,
            chess.KING: 20000
        }

        pawn_square_values = {1: 0.9, 2: 0.9, 3: 0.9, 4: 0.9, 5: 0.9, 6: 0.9, 7: 0.9, 8: 0.9,
                              9: 0.9, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 0.9,
                              17: 0.9, 18: 1.0, 19: 1.1, 20: 1.1, 21: 1.1, 22: 1.1, 23: 1.0, 24: 0.9,
                              25: 0.9, 26: 1.0, 27: 1.1, 28: 1.2, 29: 1.2, 30: 1.1, 31: 1.0, 32: 0.9,
                              33: 0.9, 34: 1.0, 35: 1.1, 36: 1.2, 37: 1.2, 38: 1.1, 39: 1.0, 40: 0.9,
                              41: 0.9, 42: 1.0, 43: 1.1, 44: 1.2, 45: 1.2, 46: 1.1, 47: 1.0, 48: 0.9,
                              49: 0.9, 50: 1.0, 51: 1.1, 52: 1.1, 53: 1.1, 54: 1.1, 55: 1.0, 56: 0.9,
                              57: 0.9, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 0.9}

        knight_square_values = pawn_square_values

        bishop_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                                9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                                17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                                25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                                33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                                41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                                49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                                57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        rook_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                              9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                              17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                              25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                              33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                              41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                              49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                              57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        queen_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                               9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                               17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                               25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                               33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                               41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                               49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                               57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        king_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                              9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                              17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                              25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                              33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                              41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                              49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                              57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        dict_of_square_values = {chess.PAWN: pawn_square_values, chess.KNIGHT: knight_square_values,
                                 chess.BISHOP: bishop_square_values, chess.ROOK: rook_square_values,
                                 chess.QUEEN: queen_square_values, chess.KING: king_square_values}

        white_material = 0
        black_material = 0

        for square in chess.SQUARES:
            piece = self.piece_at(square)
            if not piece:
                continue
            if piece.color == chess.WHITE:
                white_material += piece_values[piece.piece_type] * dict_of_square_values[piece.piece_type][square + 1]
            else:
                black_material += piece_values[piece.piece_type] * dict_of_square_values[piece.piece_type][square + 1]

        self.eval = (white_material - black_material) / 100

    def minmax(self, max_depth, current_depth, is_max_player, alpha, beta, nodes_per_depth):

        # This if else code block is only used for analysis of algorithm, by counting number of nodes explored
        if max_depth - current_depth in nodes_per_depth:
            nodes_per_depth[max_depth - current_depth] += 1
        else:
            nodes_per_depth[max_depth - current_depth] = 1

        # This is the base case, depth == 0 means it is a leaf node
        if current_depth == 0:
            self.evaluate()
            leaf_node_score = self.eval
            return leaf_node_score, nodes_per_depth

        if is_max_player:
            # set absurdly high negative value such that none of the static evaluation result less than this value
            best_score = -100000

            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))

                # pushing the current move to the board
                self.push(move)

                # calculating node score, if the current node will be the leaf node, then score will be calculated by static evaluation;
                # score will be calculated by finding max value between node score and current best score.
                node_score, nodes_per_depth = self.minmax(max_depth, current_depth - 1, self.color, alpha, beta,
                                                          nodes_per_depth)

                # calculating the max value for the particular node
                best_score = max(best_score, node_score)

                # undoing the last move, so that we can evaluate next legal moves
                self.pop()

                # alpha-beta pruning
                alpha = max(alpha, best_score)
                if alpha >= beta:
                    break

            return (best_score, nodes_per_depth)

        else:
            # set absurdly high positive value such that none of the static evaluation result more than this value
            best_score = 100000

            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))

                # pushing the current move to the board
                self.push(move)

                # calculating node score, if the current node will be the leaf node, then score will be calculated by static evaluation;
                # score will be calculated by finding min value between node score and current best score.
                node_score, nodes_per_depth = self.minmax(max_depth, current_depth - 1, True, alpha, beta,
                                                          nodes_per_depth)

                # calculating the min value for the particular node
                best_score = min(best_score, node_score)

                # undoing the last move, so that we can evaluate next legal moves
                self.pop()

                # alpha-beta pruning
                beta = min(beta, best_score)
                if alpha >= beta:
                    break

            return (best_score, nodes_per_depth)

    def best_move_using_minmax(self, max_time, is_max_player):
        start_time = time.time()
        best_move_score = -1000000
        best_move = None
        nodes_per_depth = dict()

        # start with a depth limit of 1 and increment by 1 until the time limit is reached
        depth = 1
        while time.time() - start_time < max_time:
            print(depth)
            print(time.time() - start_time)
            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))
                self.push(move)
                move_score, nodes_per_depth = self.minmax(depth, depth, False, alpha=-float('inf'), beta=float('inf'),
                                                          nodes_per_depth=nodes_per_depth)
                score = max(best_move_score, move_score)
                self.pop()
                if score > best_move_score:
                    best_move_score = score
                    best_move = move
            depth += 1

        print(best_move, nodes_per_depth)
        return (best_move, nodes_per_depth)


class Local_Player_1b(chess.Board):  # implement memorization
    def __init__(self, board, color):
        super().__init__()
        fen_parts = board.fen().split()

        self.set_board_fen(fen_parts[0])
        self.turn = board.turn
        self.eval = 0
        self.ordered_moves = []
        self.best_move = ""
        self.color = color

        # initialize the dictionary to store evaluated positions and their evaluations
        with open("evaluated_positions.json") as f:
            self.evaluated_positions = json.load(f)

    def update(self, board):
        self.set_fen(board.fen())
        print(len(self.evaluated_positions))

    def choose_best_move(self):
        print("test")
        self.best_move = self.best_move_using_minmax(max_time=10, is_max_player=self.turn)
        print(self.best_move)

    def evaluate(self):

        # check if the current position has been evaluated before
        current_position = self.board_fen()
        if current_position in self.evaluated_positions:
            self.eval = self.evaluated_positions[current_position]
            return

        piece_values = {
            chess.PAWN: 100,
            chess.ROOK: 500,
            chess.KNIGHT: 320,
            chess.BISHOP: 330,
            chess.QUEEN: 900,
            chess.KING: 20000
        }

        pawn_square_values = {1: 0.9, 2: 0.9, 3: 0.9, 4: 0.9, 5: 0.9, 6: 0.9, 7: 0.9, 8: 0.9,
                              9: 0.9, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 0.9,
                              17: 0.9, 18: 1.0, 19: 1.1, 20: 1.1, 21: 1.1, 22: 1.1, 23: 1.0, 24: 0.9,
                              25: 0.9, 26: 1.0, 27: 1.1, 28: 1.2, 29: 1.2, 30: 1.1, 31: 1.0, 32: 0.9,
                              33: 0.9, 34: 1.0, 35: 1.1, 36: 1.2, 37: 1.2, 38: 1.1, 39: 1.0, 40: 0.9,
                              41: 0.9, 42: 1.0, 43: 1.1, 44: 1.2, 45: 1.2, 46: 1.1, 47: 1.0, 48: 0.9,
                              49: 0.9, 50: 1.0, 51: 1.1, 52: 1.1, 53: 1.1, 54: 1.1, 55: 1.0, 56: 0.9,
                              57: 0.9, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 0.9}

        knight_square_values = pawn_square_values

        bishop_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                                9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                                17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                                25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                                33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                                41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                                49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                                57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        rook_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                              9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                              17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                              25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                              33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                              41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                              49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                              57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        queen_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                               9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                               17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                               25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                               33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                               41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                               49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                               57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        king_square_values = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
                              9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0,
                              17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0,
                              25: 1.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 1.0,
                              33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0,
                              41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0,
                              49: 1.0, 50: 1.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
                              57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0}

        dict_of_square_values = {chess.PAWN: pawn_square_values, chess.KNIGHT: knight_square_values,
                                 chess.BISHOP: bishop_square_values, chess.ROOK: rook_square_values,
                                 chess.QUEEN: queen_square_values, chess.KING: king_square_values}

        white_material = 0
        black_material = 0

        for square in chess.SQUARES:
            piece = self.piece_at(square)
            if not piece:
                continue
            if piece.color == chess.WHITE:
                white_material += piece_values[piece.piece_type] * dict_of_square_values[piece.piece_type][square + 1]
            else:
                black_material += piece_values[piece.piece_type] * dict_of_square_values[piece.piece_type][square + 1]

        self.eval = (white_material - black_material) / 100
        self.evaluated_positions[self.fen()] = self.eval

    def minmax(self, max_depth, current_depth, is_max_player, alpha, beta, nodes_per_depth):

        # This if else code block is only used for analysis of algorithm, by counting number of nodes explored
        if max_depth - current_depth in nodes_per_depth:
            nodes_per_depth[max_depth - current_depth] += 1
        else:
            nodes_per_depth[max_depth - current_depth] = 1

        # This is the base case, depth == 0 means it is a leaf node
        if current_depth == 0:
            self.evaluate()
            leaf_node_score = self.eval
            return leaf_node_score, nodes_per_depth

        if is_max_player:
            # set absurdly high negative value such that none of the static evaluation result less than this value
            best_score = -100000

            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))

                # pushing the current move to the board
                self.push(move)

                # calculating node score, if the current node will be the leaf node, then score will be calculated by static evaluation;
                # score will be calculated by finding max value between node score and current best score.
                node_score, nodes_per_depth = self.minmax(max_depth, current_depth - 1, self.color, alpha, beta,
                                                          nodes_per_depth)

                # calculating the max value for the particular node
                best_score = max(best_score, node_score)

                # undoing the last move, so that we can evaluate next legal moves
                self.pop()

                # alpha-beta pruning
                alpha = max(alpha, best_score)
                if alpha >= beta:
                    break

            return (best_score, nodes_per_depth)

        else:
            # set absurdly high positive value such that none of the static evaluation result more than this value
            best_score = 100000

            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))

                # pushing the current move to the board
                self.push(move)

                # calculating node score, if the current node will be the leaf node, then score will be calculated by static evaluation;
                # score will be calculated by finding min value between node score and current best score.
                node_score, nodes_per_depth = self.minmax(max_depth, current_depth - 1, True, alpha, beta,
                                                          nodes_per_depth)

                # calculating the min value for the particular node
                best_score = min(best_score, node_score)

                # undoing the last move, so that we can evaluate next legal moves
                self.pop()

                # alpha-beta pruning
                beta = min(beta, best_score)
                if alpha >= beta:
                    break

            return (best_score, nodes_per_depth)

    def best_move_using_minmax(self, max_time, is_max_player):
        start_time = time.time()
        best_move_score = -1000000
        best_move = None
        nodes_per_depth = dict()

        # start with a depth limit of 1 and increment by 1 until the time limit is reached
        depth = 1
        while time.time() - start_time < max_time:
            print(depth)
            print(f"time used{time.time() - start_time}")
            print(f"position evaluated {len(self.evaluated_positions)}")
            for legal_move in self.legal_moves:
                move = chess.Move.from_uci(str(legal_move))
                self.push(move)
                move_score, nodes_per_depth = self.minmax(depth, depth, False, alpha=-float('inf'), beta=float('inf'),
                                                          nodes_per_depth=nodes_per_depth)
                score = max(best_move_score, move_score)
                self.pop()
                if score > best_move_score:
                    best_move_score = score
                    best_move = move
            depth += 1
        with open('evaluated_positions.json', 'w') as f:
            json.dump(self.evaluated_positions, f)
            print("saved evaluated positions")

        print(best_move, nodes_per_depth)
        return (best_move, nodes_per_depth)
