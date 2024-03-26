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
    name = input('what is your name?')
    return redirect('/tape/recoding')

@trap.route('/tape/recording', methods=['GET', 'POST'])
def tape_recording():
    print ('Rise and shine' + name + 'this is a game. So many days you have wanted to die- today your aim is to live. To get get out of this room alive. Either way you win, yes? ')
    response = input('do you want to continue?')
    if response == 'yes':
        return redirect('/game')

@trap.route('/game', methods=['GET', 'POST'])
def roll():
    print ('you must roll the correct number three times')
    return redirect('/round1')

@trap.route('/round/one', methods=['GET', 'POST'])
def roll_one():
    random.randint(1, 10)
    roll_one = roll()
    if roll_one == 4:
        print(roll_one)
        print ('Congratulations, you have a second chance')
        return redirect('/round/two')
    else:
        return redirect('/death')
    
@trap.route('/round/two', methods=['GET', 'POST'])
def roll_two():
    random.randint(1, 10)
    roll_two = roll()
    if roll_two == 6:
        print(roll_two)
        print ('Congratulations, will you be able to guess the last number now?')
        return redirect('/round/three')
    else:
        return redirect('/death')
    
@trap.route('/round/three', methods=['GET', 'POST'])
def roll_three():
    random.randint(1, 10)
    roll_three = roll()
    if roll_three == 10:
        print(roll_one)
        print ('')
        return redirect('/survival')
    else:
        return redirect('/death')

@trap.route('/survival', methods=['GET', 'POST'])
def live():
    return()

@trap.route('/death', methods=['GET', 'POST'])
def die():
    print('I am surprised by you' + name + '. You did what the knight couldnt do. You have murdered an innocent man...Game over.')
    return redirect('/you/lose')

@trap.route('/you/lose', methods=['GET', 'POST'])
def serve_image():
    return render_template('image.html')