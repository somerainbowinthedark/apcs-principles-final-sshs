import random
from flask import Flask, Blueprint

trap = Blueprint('trap', __name__)
@trap.route('/start', methods=['GET', 'POST'])
def start():
    return 'Do you want to play a game?'