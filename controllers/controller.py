from code import interact
from flask import render_template # ADDED
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return render_template('index.html', title='Home')