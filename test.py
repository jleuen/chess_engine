import chess

class Local_Board_1a(chess.Board):
    def __init__(self, board):
        chess.Board.__init__(self, board)
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
        self.ordered_moves = all_moves_eval

board = chess.Board()
local_game = Local_Board_1a(board)