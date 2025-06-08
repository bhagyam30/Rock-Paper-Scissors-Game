from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ['rock', 'paper', 'scissors']

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

@app.route('/', methods=['GET', 'POST'])
def index():
    player_choice = computer_choice = result = ""
    
    if request.method == 'POST':
        player_choice = request.form['choice']
        computer_choice = random.choice(choices)
        result = determine_winner(player_choice, computer_choice)

    return render_template('index.html', player=player_choice, computer=computer_choice, result=result)

if __name__ == "__main__":
    app.run(debug=True)
