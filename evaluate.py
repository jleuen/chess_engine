import chess


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
        all_moves_eval.sort(key=lambda x: x[1], reverse=True)
        print(list(all_moves_eval))
        self.ordered_moves = list(all_moves_eval)


### Ajout de la recherche a une profondeure de 3 coups

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
        all_moves_eval.sort(key=lambda x: x[1], reverse=True)
        print(list(all_moves_eval))
        self.ordered_moves = list(all_moves_eval)
