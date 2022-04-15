
from flask import render_template
from app import app
# from models.player import *
from models.game import *


@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/<player1_choice>/<player2_choice>')
def game_page(player1_choice, player2_choice):
    game = Game()
    winner = game.play_game(player1_choice, player2_choice)
    return render_template('result.html', title='Game', winner=winner)