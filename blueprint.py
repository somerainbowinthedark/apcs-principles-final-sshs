import random
from flask import Flask, Blueprint

trap = Blueprint('trap', __name__)
@trap.route('/beginning', methods=['GET', 'POST'])
def trap():
    return 'Do you want to play a game?'
    return redirect('/tape/recoding')

@trap.route('/tape/recording', methods=['GET', 'POST'])
def tape_recording():
    return ''