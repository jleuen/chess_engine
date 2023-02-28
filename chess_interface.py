# interface du jeux d'échec
import time

import evaluate

import chess
import random


def game(partie):  # partie = chess.Board()
    white_brain = "best_move_1a"
    black_brain = "random"
    while not partie.is_game_over():
        print(partie.fen())

        #       if Board.turn() ## check if it's white turn (True) or black turn (False)
        print("global game")
        print(partie.turn)
        print(partie)
        if partie.turn:  ## check if it's white turn (True) or black turn (False)
            local_game = evaluate.Local_Board_6c(partie)

            print("White to play")
            best_move = local_game.best_move[0]
            print("best move is", best_move)
            partie.push(best_move)

        else:
            local_game = evaluate.Local_Board_5c(partie)
            print("black to play")
            best_move = local_game.ordered_moves[0][0]
            print("best move is", best_move)
            partie.push(best_move)

        print("eval is", local_game.eval)