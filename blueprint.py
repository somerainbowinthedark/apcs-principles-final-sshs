import random
from flask import Flask, Blueprint

trap = Blueprint('trap', __name__)
@trap.route('/beginning', methods=['GET', 'POST'])
def trap():
    print ('Do you want to play a game?')

@trap.route('/conversation', methods=['GET', 'POST'])
def trap():
    print ('Whats your name?')
    print ('My name is very ****ing confused!')
    name= input('what is your name?')
    return redirect('/tape/recoding')

@trap.route('/tape/recording', methods=['GET', 'POST'])
def tape_recording():
    print ('Rise and shine' + name + 'this is a game. So many days you have wanted to die- today your aim is to live. To get get out of this room alive. Either way you win, yes? ')
