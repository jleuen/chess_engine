# Token : "lip_o7oRqxRpzon7gUkg0xWY"


###upgrade lichess account to bot
# https://lichess.org/api#operation/botAccountUpgrade

import requests

url = 'https://lichess.org/api/bot/account/upgrade'
headers = {'Authorization': 'Bearer lip_o7oRqxRpzon7gUkg0xWY'}
data = ''

response = requests.post(url, headers=headers, data=data)

print(response.text)


import lichess


import berserk

session = berserk.TokenSession("lip_o7oRqxRpzon7gUkg0xWY")
client = berserk.Client(session=session)

# Get the current user's username
print(client.account.get())

#### ACCEPT CHALLENGE
for event in client.bots.stream_incoming_events():
    print(event)

    if event['type'] == 'challenge':
        client.bots.accept_challenge(event['challenge']['id'])
        print("a")
    elif event['type'] == 'gameStart':
        game_id = event['game']['id']
        print('Game started:', game_id)
        break

print("test")
print(game_id)

# get the game state
game_state = client.games.export(game_id)
print(game_state)
# get the current position
game_state.keys()
game_state['players']

if game_state['players']['white']['user']['name'] == 'bot_leuen':
    print("white")
    color = "white"
else:
    print("black")
    color = "black"

if color == "white":
    client.bots.make_move(game_id, "e2e4")


client.bots.make_move(game_id, "e7e5")
client.bots.make_move(game_id, "b8c6")
client.bots.make_move(game_id,"e5d4")
client.bots.make_move(game_id,"f8c5")

event = client.bots.stream_game_state(game_id):
opponent_move=event["state"]["moves"][-4:]


# get the opponent's last move
game_stat = client.games.export(game_id=game_id,as_pgn=True)
print(game_stat)
a=client.bots.stream_game_state(game_id)

client.bots.post_message(game_id, "hello")
client.bots.stream_game_state(game_id)

client.games.stream_game_moves(game_id)

import chess.pgn
import io
pgn2 = io.StringIO(game_stat)
game1 = chess.pgn.read_game(pgn2)
game1.mainline()
game1.mainline_moves()
# get the current position

print(game1.board())

print(game1)


# get the opponent's last move
game_stat = client.games.export(game_id=game_id,as_pgn=True)
print(game_stat)
a=client.bots.stream_game_state(game_id)

client.bots.post_message(game_id, "hello")
client.bots.stream_game_state(game_id)

client.games.stream_game_moves(game_id)

import chess.pgn
import io
pgn2 = io.StringIO(game_stat)
game1 = chess.pgn.read_game(pgn2)
game1.mainline()
game1.mainline_moves()
# get the current position


client.games.
print(game1.board())

print(game1)


client.bots.make_move("9Nm5UTQd", "e7e6")
client.bots.make_move("9Nm5UTQd", "b8c6")
client.bots.make_move("9Nm5UTQd", "c6e7")
client.bots.resign_game("9Nm5UTQd")

game_state.keys()

import lichess-bot

game_state = lichess.api.game("9Nm5UTQd")