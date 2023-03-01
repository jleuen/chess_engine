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
            start = time.time()
            local_game = evaluate.Local_Board_7d(partie)

            print("White to play")
            best_move = local_game.best_move[0]
            print("best move is", best_move)
            partie.push(best_move)
            print("time to play :", time.time() - start)

        else:
            start = time.time()
            local_game = evaluate.Local_Board_7d(partie)
            print("black to play")
            best_move = local_game.best_move[0]
            print("best move is", best_move)
            partie.push(best_move)
            print("time to play :", time.time() - start)

        print("eval is", local_game.eval)


def an_other_game(partie):
    while not partie.is_game_over():
        white_player = evaluate.Local_Player_1a(partie, "white")
        black_player = evaluate.Local_Player_1a(partie, "black")

        if partie.turn:  ## check if it's white turn (True) or black turn (False)
            print("White to play")
            white_player.update(partie)
            white_player.best_move()
            best_move = white_player.best_move[0]
            print("best move is", best_move)
            partie.push(best_move)
        else:
            print("black to play")
            best_move = black_player.best_move[0]
            print("best move is", best_move)
            partie.push(best_move)