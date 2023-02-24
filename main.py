import chess
import evaluate
import chess_interface

match1 = chess.Board()

local_game = evaluate.Local_Board_1a(match1)

chess_interface.game(match1)
