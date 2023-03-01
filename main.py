import chess
import evaluate
import chess_interface

match1 = chess.Board()
# ind_rand = evaluate.Local_Board_random(match1)
ind_2a = evaluate.Local_Board_1a(match1)
#ind_5a = evaluate.Local_Board_5a(match1)

chess_interface.an_other_game(match1)
