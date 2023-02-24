# interface du jeux d'échec
import evaluate

import chess
import random


def game(partie):  # partie = chess.Board()
    white_brain = "best_move_1a"
    black_brain = "random"
    while not partie.is_game_over():

        #       if Board.turn() ## check if it's white turn (True) or black turn (False)
        print("global game")
        print(partie)
        if partie.turn:  ## check if it's white turn (True) or black turn (False)
            local_game = evaluate.Local_Board_1a(partie)

            print("White to play")
            print(local_game)
            best_move = local_game.ordered_moves[0][0]
            print("best move is", best_move)
            partie.push(best_move)

        else:
            local_game = evaluate.Local_Board_1a(partie)
            print("black to play")
            print(local_game)
            best_move = local_game.ordered_moves[0][0]
            print("best move is", best_move)
            partie.push(best_move)
