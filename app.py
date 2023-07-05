from flask import Flask, render_template, request, jsonify
from rock_paper_scissors import play_game
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('game.html')

user_wins = 0
computer_wins = 0
draws = 0

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json.get('choice')
    global user_wins, computer_wins, draws

    game_result = play_game(user_choice)
    computer_choice = game_result['computer_choice']
    result = game_result['result']

    if result == "It's a draw!":
        draws += 1
    elif result == "You win!":
        user_wins += 1
    else:
        computer_wins += 1

    response = {
        'computer_choice': computer_choice,
        'result': result,
        'user_wins': user_wins,
        'computer_wins': computer_wins,
        'draws': draws
    }
    return jsonify(response)

@app.route('/restart', methods=['POST'])
def restart_scores():
    global user_wins, computer_wins, draws
    user_wins = 0
    computer_wins = 0
    draws = 0
    response = {
        'user_wins': user_wins,
        'computer_wins': computer_wins,
        'draws': draws
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
